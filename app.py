import os
import pickle
from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv']
app.config['UPLOAD_PATH'] = 'tmp'
model_rms = pickle.load(open('lof_rms_trained_model.pkl', 'rb'))

def Anomaly_output(x):
    if x==1:
        return "Normal"
    else:
        return "Anomaly"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in app.config['UPLOAD_EXTENSIONS']:
    	abort(400)
    else:
    	uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], 'data.csv'))
    
    
    # Load the data
    data_dir = 'tmp/'
    file_name = 'data.csv'
    df = pd.read_csv(os.path.join(data_dir, file_name), sep='\t')
    df_b1 = df.iloc[:,0].values
    
    # Calculate rms value & Predict Anomaly
    df_b1_rms = np.sqrt((np.sum(df_b1**2))/len(df_b1)) 
    op = model_rms.predict(df_b1_rms.reshape(-1,1))
    Aop = Anomaly_output(op)
    return Aop

if __name__ == '__main__':
    app.run(port=5000,debug=True)