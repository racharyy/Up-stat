import re
import csv
from automation import xytogeo
import pickle as cp
from auxilary import bin_assign,trim
from scipy.stats import entropy 
import numpy as np


file_year =[2011,2012,2013,2014,2015,2016,2017,2018]
print file_year
# Geo_dic ={}
# with open('../../data/RPD__Part_I_Crime_14_Days.csv') as fin:
# 	j=0
# 	reader = csv.DictReader(fin)
# 	for row in reader:
# 		Geo_dic[(row["X"],row["Y"])] = xytogeo(row["X"],row["Y"])[:-3]

# 		print j
# 		j=j+1
# 		# if j>10:
# 		# 	break

#Geoid Dictionary
# Geo_dic = {}
# with open('../../data/dataset3.csv',"rb") as fin:
# 	reader = csv.DictReader(fin)
# 	for row in reader:
# 		Geo_dic [(row["X"],row["Y"])] = row["GeoID"]
Geo_dic = cp.load(open("../../data/Dicts/coordtogeo_dic.p"))




#Load weather data
Weather_data = [{} for i in range(8)]
for i in range(8):
	Weather_data[i] = cp.load(open("../../data/Weather_Data/Weather_dic_201"+str(i+1)+".p","rb"))


#Demographic Data
Demo_dic = cp.load( open( "../../data/Demo_dic.p", "rb" ) )





with open('../../data/RPD__Part_I_Crime_2011_to_Present.csv') as fin:
    with open('../../data/mid_output_14.csv','wb') as csvfile:
        reader = csv.DictReader(fin)

        #fieldnames we want to keep from the original dataset and new fieldnames we want to add such as probability of certain crime type 
        orig_field = ["X","Y","OccurredFrom_Time","OccurredFrom_Date_Month","Patrol_Beat","Statute_Text","Location_Type","Geo_Section_Num"]
        add_field = ["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder",'IsNon-Negligent Manslaughter',"Ismor","Isnoon","Isnight"]
        weather_field = Weather_data[0][Weather_data[0].keys()[0]].keys()
        #print weather_field
        race_list = ["Asian","Black","White","Other"]
        age_list = []
        Season_list =["IsFall","IsSpring","IsSummer","IsWinter"]
        rest = ["PopDensity","PropRate14","Unemployed","OwnerPer","RenterPer"]
        demo_field = race_list +age_list+rest
        fieldnames = orig_field[:2]+["GeoID"]+orig_field[2:] + add_field + weather_field + demo_field+Season_list


        #creating the fieldnames for new file
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        geoid_count = {}
        normalize_restdic={}

        ind=0
        #writing in file
        for  row in reader:
            write_dict={}
            # if ind%100==0:
            #     #print ind
            ind=ind+1
            if int(row["OccurredFrom_Date_Year"]) in file_year:
                if (row["X"] and row["Y"]):
                        #Keeping the original data
                        for i in orig_field:
                                write_dict[i] = row[i]
                                op,time,seas_bin,seas = bin_assign(row["Statute_Text"],row["OccurredFrom_Time"],int(row["OccurredFrom_Date_Month"]))
                        for i in range(len(add_field)):
                                write_dict[add_field[i]] = op[i]

                        #Keeping the Month Info
                        for mnths in Season_list:
                                write_dict[mnths] = seas_bin[mnths]
            
    		        #Adding Weather data
    		        time_stamp = row["OccurredFrom_Timestamp"]
    		        if len(time_stamp)>10:
    			        year = time_stamp[:4]
    			        month = trim(time_stamp[5:7])
    			        date = trim(time_stamp[8:10])
    			        time_format = month+"/"+date+"/"+year
    
    
    			        wea_dic = Weather_data[int(year[-1])-1][time_format]
    			    	for weather_params in wea_dic:
    			    		write_dict[weather_params] = wea_dic[weather_params]
    
    			    
    
    
    
    
    		        #processing the geoid and the geoid count
    		        geoid = Geo_dic[(row["X"],row["Y"])]
    		        write_dict["GeoID"] = geoid
    		        if geoid in geoid_count:
    		        	geoid_count[geoid][0]["Is"+row["Statute_Text"]] = geoid_count[geoid][0]["Is"+row["Statute_Text"]]+1
    		        	geoid_count[geoid][1][time] = geoid_count[geoid][1][time]+1
    		        	geoid_count[geoid][2][seas] = geoid_count[geoid][2][seas]+1
    		        	
    		        else:
    		        	subdic_crm={"IsLarceny":0,"IsBurglary":0,"IsMotor Vehicle Theft":0,"IsRobbery":0,"IsAggravated Assault":0,"IsMurder":0,"IsNon-Negligent Manslaughter":0}
    		        	subdic_crm["Is"+row["Statute_Text"]]= subdic_crm["Is"+row["Statute_Text"]]+1
    		        	subdic_time = {"Ismor":0,"Isnoon":0,"Isnight":0}
    		        	subdic_time[time] =  subdic_time[time]+1
    		        	geoid_count[geoid] =  [subdic_crm,subdic_time,seas_bin]
                        if geoid in Demo_dic:

                                #write the normalized race info
                                race_nrm = 0
                                for races in race_list:
                                        race_nrm = race_nrm+int(Demo_dic[geoid][races])
                                        if race_nrm != 0:
                                                for races in race_list:
                                                        write_dict[races] = float(Demo_dic[geoid][races])/float(race_nrm)
                    
                                        # age_nrm=0
                                        # for ages in age_list:
                                        # 	age_nrm = age_nrm+int(Demo_dic[geoid][ages])
                                        # for ages in age_list:
                                        # 	write_dict[ages] = float(Demo_dic[geoid][ages])/float(age_nrm)
                                        for demos in rest:
                                            write_dict[demos] = Demo_dic[geoid][demos]
                                            if demos in normalize_restdic:
                                                #print Demo_dic[geoid][demos]
                                                if Demo_dic[geoid][demos]:
                                                    normalize_restdic[demos] = normalize_restdic[demos]+float(Demo_dic[geoid][demos])
                                            
                                                
                                            else:
                                                normalize_restdic[demos] = float(Demo_dic[geoid][demos])
                        writer.writerow(write_dict)
				
#print geoid_count

#normalize the count
with open('../../data/mid_output_14.csv') as fin:
    with open('../../data/output_'+str(file_year)+'.csv','wb') as csvfile:

        reader = csv.DictReader(fin)
        fieldnames= reader.fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        add_field = ["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder","IsNon-Negligent Manslaughter"]
        time_field = ["Ismor","Isnoon","Isnight"]

        ind=0
        for row in reader:
        	write_dict={}
        	geoid = row["GeoID"]
        	nrm_crm =  sum(geoid_count[geoid][0].values())
        	nrm_time =  sum(geoid_count[geoid][1].values())
        	nrm_seas = sum(geoid_count[geoid][2].values())
        	if nrm_crm!=0:
	        	for i in fieldnames:
	        		if i in add_field:
	        			if geoid_count[geoid][0][i]==0:
	        				write_dict[i]=0.00001
                                        else:
                                                write_dict[i] = float(geoid_count[geoid][0][i])/nrm_crm
                                # elif i in time_field:
                                #         write_dict[i] = float(geoid_count[geoid][1][i])/nrm_time
                                # elif i in Season_list:
                                #         write_dict[i] = float(geoid_count[geoid][2][i])/nrm_seas
                                        
                                elif i in rest:
                                        if normalize_restdic[i]!=0:
                                                if row[i]:
                                                        write_dict[i] =float(row[i])/normalize_restdic[i]
	        		else:
	        			write_dict[i] = row[i]

                writer.writerow(write_dict)
        	#print ind
                ind=ind +1


with open('../../data/output_'+str(file_year)+'.csv') as fin:
    with open('../../data/year_wise/Finaldata_'+str(file_year)+'.csv','wb') as csvfile:

        reader = csv.DictReader(fin)
        fieldnames= reader.fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames+["Ethnicity_Distribution"])
        writer.writeheader()
        for row in reader:
            flag=1
            for fields in fieldnames:
                if row[fields]=="":
                    flag = 0
                    break
            
            if flag:
                true_dist=[]
                for race in race_list:
                    true_dist.append(float(row[race]))
                ent=0
                for race in race_list:
                        if float(row[race])!=0:
                                ent =ent - float(row[race])* np.log(float(row[race]))
                write_dict["Ethnicity_Distribution"] = ent
                for fields in fieldnames:
                        write_dict[fields] = row[fields]
                writer.writerow(write_dict)






        	
