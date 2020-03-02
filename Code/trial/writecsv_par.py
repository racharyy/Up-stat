import csv
import copy
from automation import xytogeo

def bin_assign(crm_text,time_txt,ratio_dic,geoid):
    l=["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder","Ismor","Isnoon","Isnight"]
    op = [0 for i in l]
    n=len(op)
    for i in range(n):
        if l[i][2:]==crm_text:
            temp=l[i]
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

    if geoid in ratio_dic:
        ratio_dic[geoid][temp]=ratio_dic[geoid][temp]+1
    else:
        subdic={"IsLarceny":0,"IsBurglary":0,"IsMotor Vehicle Theft":0,"IsRobbery":0,"IsAggravated Assault":0,"IsMurder":0}
        subdic[temp]=subdic[temp]+1
        ratio_dic[geoid] = subdic

    # print op
    # print ratio_dic
    return op,ratio_dic







with open('/Users/rupamacharyya/Dropbox/Up-stat/Data/RPD__Part_I_Crime_14_Days.csv','r') as csvinput:
    with open('mid_output_14.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        i=0
        ratio ={}
        for row in csv.reader(csvinput):
            
            if row[0] == "X":

                #top_row = copy.copy(row)

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
                    geoid = xytogeo(row[0],row[1])[:-3]
                    ad_row,dic= bin_assign(crm_text,time_txt,ratio,geoid)
                    ratio = dic
                    row = row[:2]+[geoid]+[row[time_ind],row[mon_ind],row[yr_ind],row[patrol_beat_ind],row[crimetype_ind],row[loctype_ind],row[geobeat_ind],row[geosec_ind]]+ad_row
                    writer.writerow(row)

            i=i+1
            print i
            # if i>10:
            # 	break


        csvoutput.close()
    csvinput.close()
#print ratio
for i in ratio:
    x=ratio[i]
    #print i,x
    for j in x:
        norm = sum(x.values())
        #print 
        ratio[i][j] =float(ratio[i][j])/float(norm)
        



#code to change Binary to ratio

with open('mid_output_14.csv','r') as csvinput:
    with open('output_14.csv', 'w') as csvoutput:

        writer = csv.writer(csvoutput)

        i=0
        for row in csv.reader(csvinput):
            if row[0]=="X":
                ind=row.index("Statute_Text")
                ind_lar = row.index("IsLarceny")
                ind_bur = row.index("IsBurglary")
                ind_mot = row.index("IsMotor Vehicle Theft")
                ind_rob = row.index("IsRobbery")
                ind_agg = row.index("IsAggravated Assault")
                ind_mur = row.index("IsMurder")
                # ind_lar = row.index("Ismor")
                # ind_lar = row.index("Isnoon")
                # ind_lar = row.index("Isnight")
   

            if row[0] != "X":
                geoid = row[2]
                row[ind_lar] =  ratio[geoid]["IsLarceny"]
                row[ind_bur] =  ratio[geoid]["IsBurglary"]
                row[ind_mot] =  ratio[geoid]["IsMotor Vehicle Theft"]
                row[ind_rob] =  ratio[geoid]["IsRobbery"]
                row[ind_agg] = ratio[geoid]["IsAggravated Assault"]
                row[ind_mur] = ratio[geoid]["IsMurder"]

            writer.writerow(row)


            i=i+1
            print i

