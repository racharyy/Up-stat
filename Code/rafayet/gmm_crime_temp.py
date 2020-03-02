import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from sklearn.mixture import GMM
from sklearn.mixture import GaussianMixture

file_crime  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
time_crime = file_crime['OccurredFrom_Timestamp']

file_wet  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Code/rafayet/KROC_daily_rafayet.csv')
time_wet = file_wet['Date']
Avg_Temp = file_wet['Avg Temp']

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

# print(crime_temp_list[0])
crime_temp_array = np.zeros([len(crime_temp_list),1])
for i in range(len(crime_temp_list)):
	crime_temp_array[i][0] = int(crime_temp_list[i])
# print (crime_temp_array, crime_temp_array.T.shape)
# crime_temp_array = crime_temp_array.T

# N = np.arange(1, 11)
# models = [None for i in range(len(N))]

# for i in range(len(N)):
    # models[i] = GMM(N[i]).fit(crime_temp_array)
# AIC = [m.aic(crime_temp_array) for m in models]
# BIC = [m.bic(crime_temp_array) for m in models]

M_best = GaussianMixture(2).fit(crime_temp_array)

# M_best = models[np.argmin(BIC)]
# print (M_best ,AIC,BIC )

x = np.linspace(10, 100, 1000)
x_t = np.zeros([len(x),1])
for i in range(len(x)):
	x_t[i][0] = int(x[i])
	
logprob = M_best.predict_proba(x_t)
pdf = np.exp(logprob)
# pdf_individual = responsibilities * pdf[:, np.newaxis]

print (pdf)

plt.hist(crime_temp_array, 30, histtype='stepfilled', alpha=0.4)
plt.plot(x_t, pdf, '-k')
plt.show()