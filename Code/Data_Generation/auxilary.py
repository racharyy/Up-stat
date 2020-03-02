import numpy
import scipy as sp

def bin_assign(crm_text,time_txt,mnth_text):
    seas_bin = {"IsFall":0,"IsSpring":0,"IsSummer":0,"IsWinter":0}
    l=["IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder","IsNon-Negligent Manslaughter","Ismor","Isnoon","Isnight"]
    op = [0 for i in l]
    n=len(op)
    time=""
    seas=""
    time_txt = int(time_txt)
    for i in range(n):
        if l[i][2:]==crm_text:
            temp=l[i]
            op[i]=1

        if (time_txt<=1500 and time_txt>900):
        	if l[i]=="Ismor":
        		op[i]=1
        		time = "Ismor"
        		
        elif (time_txt<=2100 and time_txt>1500):
        	if l[i]=="Isnoon":
        		op[i]=1
        		time = "Isnoon"
        		
        else:
        	if l[i]=="Isnight":
        		op[i]=1
        		time = "Isnight"

    if (mnth_text>=2 and mnth_text<=4):
        seas_bin["IsSpring"]=1
        seas="IsSpring"
    elif (mnth_text>=5 and mnth_text<=7):
        seas_bin["IsSummer"]=1
        seas="IsSummer"
    elif (mnth_text>=8 and mnth_text<=10):
        seas_bin["IsFall"]=1
        seas="IsFall"
    else:
        seas_bin["IsWinter"]=1
        seas="IsWinter"

        
        		


    return op,time,seas_bin,seas


#trims the 0 from month and date   
def trim(s):
	x=s
	if s[0]=='0':
		x= s[1]
	return x




