#Schuyler Mortimer Honors Thesis
import pandas as pd
import csv

df = pd.read_csv("/home/schuyler/Desktop/Honors_Thesis/data_sets/master_data.csv")

dates_count = {}

#Adds new dates to dates_count dictionary, incraments by one if already in dictionary
for date in df["date"]:
    temp_date = date[0:10]

    if temp_date not in dates_count:
        dates_count[temp_date] = 1
    else:
        dates_count[temp_date] += 1

#Print line is just for debug purposes
for k, v in dates_count.items():
    print v, k

#Writes the dictionary to a CSV
with open("/home/schuyler/Desktop/Honors_Thesis/data_sets/date_counts.csv", "wb") as dates:

    try:
        dates.truncate()
    except:
        pass

    writer = csv.writer(dates)
    writer.writerow(["Count", "Date"])

    for k, v in dates_count.items():
        writer.writerow([v,k])
