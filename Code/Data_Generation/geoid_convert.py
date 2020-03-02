import csv
from automation import xytogeo
import pickle as cp







with open('../../data/RPD__Part_I_Crime_2011_to_Present.csv') as fin:
	with open('../../data/dataset7.csv','wb') as csvfile:
		j=0
		reader = csv.DictReader(fin)
		fieldnames =["X","Y","GeoID"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row	in reader:
			j=j+1
			
			if (j>56900 and j<57400):
				if (row["X"]and row["Y"]):
					if j%100 ==0:
						print j
					write_dic={}
					write_dic["X"] = row["X"]
					write_dic["Y"] = row["Y"]
					write_dic["GeoID"] = xytogeo(row["X"],row["Y"])[:-3]
					writer.writerow(write_dic)
				
				






        # for row in reader:
        # 	if (row["X"] and row["Y"]):
	       #  	write_dic={}
	       #  	write_dic["X"] = row["X"]
	       #  	write_dic["Y"] = row["Y"]
	       #  	write_dic["GeoID"] = xytogeo(row["X"],row["Y"])[:-3]
	       #  	print write_dic
	       #  	writer.writerow(write_dic)
	        	
# 		# if j>10:
# 		# 	break