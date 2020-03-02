import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

file_crime  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
time_crime = file_crime['OccurredFrom_Timestamp']

file_wet  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Code/rafayet/KROC_daily_rafayet.csv')
time_wet = file_wet['Date']
Avg_Temp = file_wet['Avg Temp']
snow = file_wet['Snowfall']

	# print(c_date)
temp_dict = dict()
snow_dict = dict()
for t in range(len(time_wet)):
	month,day,year  = (int(x) for x in time_wet[t].split('-'))
	year = year+2000
	# print(month,day,year)
	c_date = datetime.date(year, month, day)
	temp_dict[c_date] = Avg_Temp[t]
	snow_dict[c_date] = snow[t]

month_temp = np.zeros([12])
crime_month = np.zeros([12])
snow_month = np.zeros([12])

for t in time_crime:
	dt = t[:t.index('T')]
	year, month,day  = (int(x) for x in dt.split('-'))
	c_date = datetime.date(year, month, day)
	if np.isnan(temp_dict[c_date]) == False:
		crime_month[month-1] += 1
		month_temp[month-1] +=  np.nan_to_num(temp_dict[c_date])
		snow_month[month-1] += np.nan_to_num(snow_dict[c_date])

print (month_temp/crime_month , crime_month/np.sum(crime_month))
month_temp = month_temp/crime_month

snow_month = (snow_month/crime_month)*1000
crime_month = crime_month/np.sum(crime_month)*100
plt.scatter(month_temp, crime_month, alpha=0.5)
# fig, ax = plt.subplots()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep' , 'Oct', 'Nov', 'Dec' ]
for i in range(12):
    plt.annotate(months[i], (month_temp[i]+1,crime_month[i]+0))
plt.ylabel('Crime Percentage')
plt.xlabel('Temperature')
plt.title('Temp vs Crime by Month' )
plt.savefig('Temp vs Crime by Month.png')
plt.clf()
# plt.show()

# exit(1)


crime = file_crime['Statute_Text']
crime_set = set(crime)
crime_set = sorted(crime_set)
time = file_crime['OccurredFrom_Timestamp']
for c in crime_set:
	time_list = time[crime == c]
	month_temp = np.zeros([12])
	crime_month = np.zeros([12])
	snow_month = np.zeros([12])
	for t in time_list:
		dt = t[:t.index('T')]
		year, month,day  = (int(x) for x in dt.split('-'))
		c_date = datetime.date(year, month, day)
		if np.isnan(temp_dict[c_date]) == False:
			crime_month[month-1] += 1
			month_temp[month-1] +=  np.nan_to_num(temp_dict[c_date])
			snow_month[month-1] += np.nan_to_num(snow_dict[c_date])
	
	for i in range(12):
		if crime_month[i] >0:
			month_temp[i] = month_temp[i]/crime_month[i]
	crime_month = crime_month/np.sum(crime_month)*100
	plt.scatter(month_temp, crime_month, alpha=0.5)
	for i in range(12):
		plt.annotate(months[i], (month_temp[i]+1,crime_month[i]+0))
	plt.ylabel(str(c)+' Percentage')
	plt.xlabel('Temperature')
	plt.savefig('Temp vs '+str(c)+' by Month.png')
	plt.clf()

	