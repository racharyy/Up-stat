import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

file_crime  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
time_crime = file_crime['OccurredFrom_Timestamp']

file_wet  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Code/rafayet/KROC_daily_rafayet.csv')
time_wet = file_wet['Date']
Avg_Temp = file_wet['Avg Temp']


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
	
bin_size = 20
n, bins, patches = plt.hist(crime_temp_list, bin_size, normed=1, facecolor='green', alpha=0.5)
plt.title('Crimes by temperature')
plt.ylabel('Crime Percentage')
plt.xlabel('Temperature in Fahrenheit')
# plt.show()
plt.savefig('Crime by temperature.png')
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

	n, bins, patches = plt.hist(crime_temp_list, bin_size, normed=1, facecolor='green', alpha=0.5)
	plt.title(str(c)+' by temperature')
	plt.ylabel(str(c)+' Percentage')
	plt.xlabel('Temperature in Fahrenheit')
	# plt.show()
	plt.savefig(str(c)+' by temperature.png')
	plt.clf()
	