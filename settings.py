PROJECT_NAME_ID_MAP = { 
	'ebolaresponse' : 93,
	'somalidrought' : 94,
	'emergencyshelterassessmentinthemiddleeast' : 95,
	'yamunamonsoonflooding2013' : 96,
	'yemeniculturalheritageatrisk' : 97
	}

GEOTAGX_HOST = "http://geotagx.org"
GEOKEY_HOST = "http://play.geokey.org.uk"

GEOTAGX_GEOJSON_URL_TEMPLATE = GEOTAGX_HOST+"/geotagx/export/category/%s/GeoJSON"
GEOKEY_POST_TEMPLATE = GEOKEY_HOST+"/api/geotagx/%s/import/"
GEOKEY_MAP_TEMPLATE = GEOKEY_HOST+"/geotagx/%s/"
