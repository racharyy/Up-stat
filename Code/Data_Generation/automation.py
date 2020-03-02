#(X,Y) coordinate to GeoID

import urllib2
import json


def xytogeo(X,Y):
    # X = Put the longitude
    # Y = Put the latitude
    txt = urllib2.urlopen('https://geo.fcc.gov/api/census/block/find?latitude={1}&longitude={0}&format=json'.format(X,Y)).read()
    result = json.loads(txt)
    #print result
    # Also check the other fields of the result dictionary
    return result['Block']['FIPS']


