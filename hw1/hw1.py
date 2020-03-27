# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061146.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

C0A880_mean = []
C0F9A0_mean = []
C0G640_mean = []
C0R190_mean = []
C0X260_mean = []

result = []

for x in data:
    if (x['PRES'] == '-999.000') or (x['PRES'] == '-99.000') :
        i=1
    else:
        if (x['station_id'] == 'C0A880'):
            C0A880_mean.append(float(x['PRES']))
        if (x['station_id'] == 'C0F9A0'):
            C0F9A0_mean.append(float(x['PRES']))
        if (x['station_id'] == 'C0G640'):
            C0G640_mean.append(float(x['PRES']))
        if (x['station_id'] == 'C0R190'):
            C0R190_mean.append(float(x['PRES']))
        if (x['station_id'] == 'C0X260'):
            C0X260_mean.append(float(x['PRES']))

if len(C0A880_mean) != 0:
    result.append(['C0A880', sum(C0A880_mean) / len(C0A880_mean)])
else:
    result.append(['C0A880', 'None'])
if len(C0F9A0_mean) != 0:
    result.append(['C0F9A0', sum(C0F9A0_mean) / len(C0F9A0_mean)])
else:
    result.append(['C0F9A0', 'None'])
if len(C0G640_mean) != 0:
    result.append(['C0G640', sum(C0G640_mean) / len(C0G640_mean)])
else:
    result.append(['C0G640', 'None'])
if len(C0R190_mean) != 0:
    result.append(['C0R190', sum(C0R190_mean) / len(C0R190_mean)])
else:
    result.append(['C0R190', 'None'])
if len(C0X260_mean) != 0:
    result.append(['C0X260', sum(C0X260_mean) / len(C0X260_mean)])
else:
    result.append(['C0X260', 'None'])



#=======================================

# Part. 4
#=======================================
# Print result
print(result)
#========================================