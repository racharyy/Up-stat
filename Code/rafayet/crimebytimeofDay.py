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
	hour_crime = np.zeros([24])
	for t in time_list:
		# print (t)		
		dt = int(t[t.index('T')+1:t.index(':')])
		
		# print (dt)
		hour_crime[dt] +=1
		
	hour_crime = hour_crime/len(time_list)*100
	print (hour_crime)
	y_pos = np.arange(24)
	plt.bar(y_pos, hour_crime,0.8,align='center', alpha=0.5)
	plt.xticks(y_pos, [i for i in range(24)])
	plt.ylabel(str(c) +' percentage' )
	plt.xlabel(' Time of day in Hours' )
	# plt.ylim([0,60])
	plt.xlim([-1,24])
	plt.title(str(c)+' by Hours of Day')
	plt.savefig( str(c)+ 'byHoursofDay.png')
	plt.clf()
	
time_list = time
hour_crime = np.zeros([24])
for t in time_list:
	# print (t)		
	dt = int(t[t.index('T')+1:t.index(':')])
	hour_crime[dt] +=1
	
hour_crime = hour_crime/len(time_list)*100
print (hour_crime)
y_pos = np.arange(24)
plt.bar(y_pos, hour_crime,0.8,align='center', alpha=0.5)
plt.xticks(y_pos, [i for i in range(24)])
plt.xlim([-1,24])
plt.ylabel('Crime percentage' )
plt.xlabel(' Time of day in Hours' )
plt.title('Crime by Hours of Day')
plt.savefig( 'CrimebyHoursofDay.png')
plt.clf()