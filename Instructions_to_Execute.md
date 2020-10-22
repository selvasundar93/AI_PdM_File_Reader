# AI Techniques for Predictive Maintenance
## Instructions to Execute 
* Open the URL "https://ai-pdm-file.herokuapp.com/"
* Upload the CSV file, which contains the 1 second vibration signal of Bearing and click Submit
* The application will respond back with result as either Normal or Anomaly

#### Note:
* Two outputs are possible (Anomaly Detection - Univariate): Normal, Anomaly
	* __Normal__ : Vibrations in Normal Range - Healthy State
	* __Anomaly__: Vibrations exceeds Normal Range - Unhealthy / Possibility of failure in near future
* Refer Data folder for the 1 second vibration signal data
* Only CSV filetype is accepted, other filetypes will result in Bad Request