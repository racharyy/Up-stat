import re
import csv
import pickle as cp
#from automation import xytogeo

Dic_list = [{} for i in range(8)]


with open('../../data/KROC_daily_edited.csv') as fin:
    
    reader = csv.DictReader(fin)
    params_to_keep = ["Avg Temp","Snowfall"]
    for row in reader:
    	date = row["Date"]
        sub_dic = {}
        for params in params_to_keep:
    	   sub_dic[params] = row[params]
    	x = int(date[-1])
    	Dic_list[x-1][date]=sub_dic
    	


for i in range(8):
	cp.dump( Dic_list[i], open( "../../data/Weather_Data/Weather_dic_201"+str(i+1)+".p", "wb" ) )



