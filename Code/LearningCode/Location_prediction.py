import pickle as cp
import numpy as np 
from automation import xytogeo

GeoKey_dic =cp.load(open( "../../data/Dicts/Geotocord_dic.p"))

def nearest(X,Y,geoid):
	coords =GeoKey_dic[geoid]
	dist = np.inf 
	near_loc = ('0','0')
	for i in coords:
		d_temp = (int(X)-int(i[0]))**2 + (int(Y)-int(i[1]))**2
		if d_temp < dist:
			dist  = d_temp
			near_loc = i

	return near_loc



def get_paramforpredicition(X,Y):

	geoid = xytogeo(X,Y)
	near_loc = nearest(X,Y,geoid)
	params = Parameter_set[near_loc]
	return params
	
	
	


	
