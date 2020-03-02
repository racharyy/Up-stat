import csv
import pickle as cp

GeoKey_dic={}
with open('../../data/dataset3.csv') as fin: 
	reader = csv.DictReader(fin)
	for row in reader:
		if row["GeoID"] in GeoKey_dic:
			GeoKey_dic[row["GeoID"]].add((row["X"],row["Y"]))
		else:
			GeoKey_dic[row["GeoID"]]=set([(row["X"],row["Y"])])

with open('../../data/dataset4.csv') as fin: 
	reader = csv.DictReader(fin)
	for row in reader:
		if row["GeoID"] in GeoKey_dic:
			GeoKey_dic[row["GeoID"]].add((row["X"],row["Y"]))
		else:
			GeoKey_dic[row["GeoID"]]=set([(row["X"],row["Y"])])


with open('../../data/dataset5.csv') as fin: 
	reader = csv.DictReader(fin)
	for row in reader:
		if row["GeoID"] in GeoKey_dic:
			GeoKey_dic[row["GeoID"]].add((row["X"],row["Y"]))
		else:
			GeoKey_dic[row["GeoID"]]=set([(row["X"],row["Y"])])


cp.dump(GeoKey_dic,open( "../../data/Dicts/Geotocord_dic.p",'wb'))
