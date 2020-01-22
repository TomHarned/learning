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

high_temps_sf = high_temps.copy()
low_temps_sf = low_temps.copy()
dates_sf = dates.copy()

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.ylim(0, 110)
plt.plot(dates_sf, high_temps_sf, c='red', alpha=0.5)
plt.plot(dates_sf, low_temps_sf, c='blue', alpha=0.5)
plt.fill_between(dates_sf, high_temps_sf,\
                 low_temps_sf, facecolor='blue', alpha=0.1)
plt.title("San Fran")
plt.xticks(rotation=45)

filename = 'data/death_valley_2014.csv'

# Get dates and high temperatures from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

high_temps_dv = highs.copy()
low_temps_dv = lows.copy()
dates_dv = dates.copy()

plt.subplot(1, 2, 2)
plt.ylim(0, 110)
plt.xticks(rotation=45)
plt.plot(dates_dv, high_temps_dv, c='red', alpha=0.5)
plt.plot(dates_dv, low_temps_dv, c='blue', alpha=0.5)
plt.title("Death Valley")
plt.fill_between(dates_dv, high_temps_dv,\
                 low_temps_dv, facecolor='blue', alpha=0.1)
plt.show()
