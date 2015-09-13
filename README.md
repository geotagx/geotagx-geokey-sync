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

#Quick Tips
----------
You can setup a cronjob to run this at particular intervals to time to keep your project in sync with the UNASIGN data feed
You can learn more about cronjobs here : http://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800

#Author
-------
S.P. Mohanty <sp.mohanty@cern.ch>