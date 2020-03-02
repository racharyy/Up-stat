import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


file  = pd.read_csv('C:/Users/Rafayet/Dropbox/Up-stat/Data/RPD__Part_I_Crime_2011_to_Present.csv')
month = file['OccurredFrom_Date_Month'].tolist()
y = []
for m in range(1,13):
	c = file[(file['OccurredFrom_Date_Month'] == m)]
	
	y.append((c.shape[0]/len(month))*100)
	print(y[-1])
	# exit(1)
# print(month) 
# N = len(y)
# x = range(N)
# width = 1/1.5
# plt.bar(x, y, width, color="blue")
# fig = plt.gcf()
# plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')



objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep' , 'Oct', 'Nov', 'Dec' )
y_pos = np.arange(len(objects))

plt.bar(y_pos, y,0.5, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Crimes')
plt.title('Crimes by Months')
plt.xlim([-1,13])
plt.savefig('Crimes by Months.png')
# plt.show()
plt.clf()

crime_type = file['Statute_Text'].tolist()
crime_type = set(crime_type)
crime_type = sorted(crime_type)
for crime in crime_type:
	y = []
	p = file[(file['Statute_Text']==crime)]
	p = p.shape[0]
	print(crime)
	for m in range(1,13):
		c = file[(file['OccurredFrom_Date_Month'] == m) & (file['Statute_Text']==crime)]
		y.append((c.shape[0]/p)*100)
		print(y[-1])
	plt.bar(y_pos, y,0.5, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel(str(crime)+ ' Percentage')
	plt.xlim([-1,13])
	plt.title(str(crime)+' by Months')
	plt.savefig( str(crime)+ ' by Months.png')
	plt.clf()

