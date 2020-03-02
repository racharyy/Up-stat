import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

file_crime  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
time_crime = file_crime['OccurredFrom_Timestamp']

file_wet  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Code/rafayet/KROC_daily_rafayet.csv')
time_wet = file_wet['Date']
Avg_Temp = file_wet['Snowfall']


	# print(c_date)
temp_dict = dict()
for t in range(len(time_wet)):
	month,day,year  = (int(x) for x in time_wet[t].split('-'))
	year = year+2000
	# print(month,day,year)
	c_date = datetime.date(year, month, day)
	temp_dict[c_date] = Avg_Temp[t]

crime_temp_list = []

for t in time_crime:
	dt = t[:t.index('T')]
	year, month,day  = (int(x) for x in dt.split('-'))
	c_date = datetime.date(year, month, day)
	crime_temp_list.append(temp_dict[c_date])
crime_temp_list = np.nan_to_num(crime_temp_list)
print (crime_temp_list)
bin_size = 10
n, bins, patches = plt.hist(crime_temp_list, bin_size, normed=1, facecolor='green', alpha=0.5)
plt.title('Crimes by Snowfall')
plt.ylabel('Crime Percentage')
plt.xlabel('Snowfall')
# plt.show()
plt.savefig('Crime by Snowfall.png')
plt.clf()


crime = file_crime['Statute_Text']
crime_set = set(crime)
crime_set = sorted(crime_set)
time = file_crime['OccurredFrom_Timestamp']
for c in crime_set:
	time_list = time[crime == c]
	crime_temp_list = []
	for t in time_list:
		dt = t[:t.index('T')]
		year, month,day  = (int(x) for x in dt.split('-'))
		c_date = datetime.date(year, month, day)
		crime_temp_list.append(temp_dict[c_date])
	crime_temp_list = np.nan_to_num(crime_temp_list)
	n, bins, patches = plt.hist(crime_temp_list, bin_size, normed=1, facecolor='green', alpha=0.5)
	plt.title('Crimes by Snowfall')
	plt.ylabel(str(c)+' Percentage')
	plt.xlabel('Snowfall')
	# plt.show()
	plt.savefig(str(c)+' by Snowfall.png')
	plt.clf()
	