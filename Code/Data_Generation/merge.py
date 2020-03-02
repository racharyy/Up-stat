import csv
from automation import xytogeo
import pickle as cp





faltu_kaaj =[]

with open('../../data/RPD__Part_I_Crime_2011_to_Present.csv') as fin:
	j=0
	reader = csv.DictReader(fin)
	for row	in reader:

		if j >=56600:
			if (row["X"] and row["Y"]):
				faltu_kaaj.append((row["X"],row["Y"]))
				print j
		j=j+1

with open('../../data/dataset5.csv') as fin:
	with open('../../data/datasetbal.csv','wb') as csvfile:
		reader = csv.DictReader(fin)
		fieldnames =["X","Y","GeoID"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		j=0
		for row in reader:
			write_dic={}
			write_dic["X"] = faltu_kaaj[j][0]
			write_dic["Y"] = faltu_kaaj[j][1]
			write_dic["GeoID"] = row["GeoID"]
			writer.writerow(write_dic)
			print j
			j=j+1




	
				

