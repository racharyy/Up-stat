import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

file  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
time = file['OccurredFrom_Timestamp'].tolist()
crime = file['Statute_Text'].tolist()
crime_set = set(crime)
crime_set = sorted(crime_set)
crime = np.array(crime)
time = np.array(time)
# print (time[crime == 'Robbery'])
y = []
days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']


for c in crime_set:
	time_list = time[crime == c]
	day_crime = np.zeros([7])
	for t in time_list:
		# print (t)		
		dt = t[:t.index('T')]
		# print (dt)
		year, month,day  = (int(x) for x in dt.split('-'))    
		ans = datetime.date(year, month, day)
		d = ans.strftime("%A")
		# print (days.index(d),d)
		day_crime[days.index(d)] +=1
	day_crime = day_crime/len(time_list)*100
	print (day_crime)
	y_pos = np.arange(7)
	plt.bar(y_pos, day_crime,0.7, align='center', alpha=0.5)
	plt.xticks(y_pos, [i[:3] for i in days])
	plt.ylabel(str(c) +' percentage' )
	# plt.ylim([0,60])
	plt.title(str(c)+' by Days')
	plt.savefig( str(c)+ ' by Days.png')
	plt.clf()
	
time_list = time
day_crime = np.zeros([7])
for t in time_list:
	# print (t)		
	dt = t[:t.index('T')]
	# print (dt)
	year, month,day  = (int(x) for x in dt.split('-'))    
	ans = datetime.date(year, month, day)
	d = ans.strftime("%A")
	# print (days.index(d),d)
	day_crime[days.index(d)] +=1
day_crime = day_crime/len(time_list)*100
print (day_crime)
y_pos = np.arange(7)
plt.bar(y_pos, day_crime,0.7, align='center', alpha=0.5)
plt.xticks(y_pos, [i[:3] for i in days])
plt.ylabel(' percentage' )
# plt.ylim([0,60])
plt.title('Crime by Days')
plt.savefig('Crimes by Days.png')
plt.clf()