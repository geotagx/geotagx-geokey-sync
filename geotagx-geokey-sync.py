import urllib2
import json
import requests

from settings import *


def collect_geojson_data(project_name):
	print "Downloading GeoJSON summary for : ",project_name
	response = urllib2.urlopen(GEOTAGX_GEOJSON_URL_TEMPLATE%project_name)
	print "GeoJSON summary successfully obtained for ",project_name
	return response.read()

def push_data_to_geokey(data, project_name, project_id):
	print "Pushing data of project : "+project_name+" to project_id : "+str(project_id)+" on "+GEOKEY_HOST


	url = GEOKEY_POST_TEMPLATE % str(project_id)
	response = requests.post(url, json=json.loads(data))
	print "Map Accessible at : ", GEOKEY_MAP_TEMPLATE % str(project_id)
	print response.content
	return response

for _project_name in PROJECT_NAME_ID_MAP.keys():
	print "="*80
	geojson_data = collect_geojson_data(_project_name)
	geokey_response = push_data_to_geokey(geojson_data, _project_name, PROJECT_NAME_ID_MAP[_project_name])