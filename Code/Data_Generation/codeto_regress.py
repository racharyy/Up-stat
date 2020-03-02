import libpysal
from gwr.gwr import GWR
import numpy as np
import csv

with open('../../data/output_14.csv') as fin:
    reader = csv.DictReader(fin)
    fieldnames= reader.fieldnames


Data_ar = []
Restricted = ["X","Y","GeoID", "OccurredFrom_Time",   "OccurredFrom_Date_Month", "Patrol_Beat", "Statute_Text","Location_Type", "Geo_Section_Num","IsLarceny","IsBurglary","IsMotor Vehicle Theft","IsRobbery","IsAggravated Assault","IsMurder"]
print len(fieldnames)-len(Restricted)
data = libpysal.open("../../data/output_14.csv")
coords = zip(data.by_col('X'), data.by_col('Y')) 
y = np.array(data.by_col('IsLarceny')).reshape((-1,1))
for fields in fieldnames:
    if fields not in Restricted:
        Data_ar.append(np.array(data.by_col(fields)).reshape((-1,1)))
X = np.hstack(Data_ar)
print X.shape
model = GWR(coords, y, X, bw=90.000, fixed=False, kernel='bisquare')
results = model.fit()
print results.params.shape