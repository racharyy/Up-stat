import csv
import copy
from automation import xytogeo

def bin_assign(crm_text,time_txt):
	l=["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder","Ismor","Isnoon","Isnight"]
	op = [0 for i in l]
	n=len(op)
	for i in range(n):
		if l[i][2:]==crm_text:
			op[i]=1
		if (time_txt<=1500 and time_txt>900):
			if l[i]=="Ismor":
				op[i]=1
		elif (time_txt<=2100 and time_txt>1500):
			if l[i]=="Isnoon":
				op[i]=1
		else:
			if l[i]=="Isnight":
				op[i]=1
	return op



#Code to change categorical Data to Binary Data

with open('/Users/rupamacharyya/Dropbox/Up-stat/Data/RPD__Part_I_Crime_14_Days.csv','r') as csvinput:
    with open('output_14.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        i=0
        for row in csv.reader(csvinput):
        	
            if row[0] == "X":

            	top_row = copy.copy(row)

            	#Finding necessary information to keep
            	time_ind= row.index("OccurredFrom_Time")
            	mon_ind= row.index("OccurredFrom_Date_Month")
            	yr_ind = row.index("Reported_Date_Year")
            	patrol_beat_ind = row.index("Patrol_Beat")
            	crimetype_ind = row.index("Statute_Text")
            	loctype_ind = row.index("Location_Type")
            	geobeat_ind = row.index("Geo_Beat")
            	geosec_ind = row.index("Geo_Section_Num")
            	row=row[:2]+["GeoID"]+[row[time_ind],row[mon_ind],row[yr_ind],row[patrol_beat_ind],row[crimetype_ind],row[loctype_ind],row[geobeat_ind],row[geosec_ind]]

            	#writing the necessary information and adding the binary datatype
                writer.writerow(row+["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder","Ismor","Isnoon","Isnight"])
            else:
            	if (row[0] and row[1]):
            		crm_text = row[crimetype_ind]
            		time_txt = int(row[time_ind])
            		ad_row= bin_assign(crm_text,time_txt)
            		row=row[:2]+[xytogeo(row[0],row[1])[:-3]]+[row[time_ind],row[mon_ind],row[yr_ind],row[patrol_beat_ind],row[crimetype_ind],row[loctype_ind],row[geobeat_ind],row[geosec_ind]]+ad_row
                	writer.writerow(row)

            i=i+1
            print i
            # if i>10:
            # 	break