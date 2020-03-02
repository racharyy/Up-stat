import re
import csv
import pickle as cp


Demo_dic = {}
with open('../../data/FinalDataTable_Website.csv') as fin:


	reader = csv.DictReader(fin)
	params_to_keep = ["PopDensity","PropRate14","Unemployed","Asian","Black","White","Other","OwnerPer","RenterPer"]
	for row in reader:
		sub_dic={}
		for i in params_to_keep:
			sub_dic[i] = row[i]


		Demo_dic[row["GeoID"]] = sub_dic




cp.dump( Demo_dic, open( "../../data/Demo_dic.p", "wb" ) )


