import csv
import pickle as cp


Geo_dic = {}
with open('../../data/dataset3.csv',"rb") as fin1:
	reader1 = csv.DictReader(fin1)
	for row in reader1:
		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]

with open('../../data/dataset4.csv',"rb") as fin2:
	reader2 = csv.DictReader(fin2)
	for row in reader2:
		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]

with open('../../data/datasetbal.csv',"rb") as fin3:
	reader3 = csv.DictReader(fin3)
	for row in reader3:
		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]

# with open('../../data/dataset6.csv',"rb") as fin:
# 	reader = csv.DictReader(fin)
# 	for row in reader:
# 		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]

# with open('../../data/dataset7.csv',"rb") as fin:
# 	reader = csv.DictReader(fin)
# 	for row in reader:
# 		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]


cp.dump(Geo_dic,open( "../../data/Dicts/coordtogeo_dic.p",'wb'))
