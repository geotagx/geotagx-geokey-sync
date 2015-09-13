#GeotagX-GeoKey-Sync
--------------------

A syncying script to export geotagx geojson summary with GeoKey

#Usage
------
```
git clone http://github.com/geotagx/geotagx-geokey-sync
cd geotagx-geokey-sync
pip install -r requirements.txt
#Edit settings.py to modify the geotagx-project-name to geokey-project_id mapping and other params
python geotagx-geokey-sync.py
```

#Creation of Projects on GeoKey
-------------------------------
* Go to http://play.geokey.org.uk/ and log in
* Create a project name it whatever you want. 
* After creating a project, create a category named ‘Result’, the name must be ‘Result’ otherwise the upload won’t work.
* Update the project_name and project id mapping in `settings.py`


#Quick Tips
----------
You can setup a cronjob to run this at particular intervals to time to keep your project in sync with the UNASIGN data feed
You can learn more about cronjobs here : http://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800

#Exported Results
-----------------
*	GeoTag-X Project Name :  ebolaresponse  
	GeoKey Map : http://play.geokey.org.uk/geotagx/93/
*	GeoTag-X Project Name :  emergencyshelterassessmentinthemiddleeast  
	GeoKey Map : http://play.geokey.org.uk/geotagx/95/
*	GeoTag-X Project Name :  yemeniculturalheritageatrisk  
	GeoKey Map : http://play.geokey.org.uk/geotagx/97/
*	GeoTag-X Project Name :  yamunamonsoonflooding2013  
	GeoKey Map : http://play.geokey.org.uk/geotagx/96/
*	GeoTag-X Project Name :  somalidrought  
	GeoKey Map : http://play.geokey.org.uk/geotagx/94/

#Author
-------
S.P. Mohanty <sp.mohanty@cern.ch>