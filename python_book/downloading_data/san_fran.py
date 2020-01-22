import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'temperature.csv'

with open(filename, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    dates, low_temps, high_temps = [], [], []

    for row in reader:
        try:
            high_temp = int(row[4])
            low_temp = int(row[5])
            date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print('error')
        else:
            high_temps.append(high_temp)
            low_temps.append(low_temp)
            dates.append(date)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, high_temps, c='red', alpha=0.5)
plt.plot(dates, low_temps, c='blue', alpha=0.5)
plt.fill_between(dates, high_temps, low_temps,\
                 facecolor='blue', alpha=0.25) 
plt.show()
