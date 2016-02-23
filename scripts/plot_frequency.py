#Schuyler Mortimer Honors Thesis
import matplotlib.pyplot as plt
import pandas as pd
import csv

def import_data():
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/date_counts.csv', 'rb') as f:
        reader = csv.reader(f)
        temp = list(reader)

        date = []
        count = []

        first_line = True

        for row in temp:

            if first_line:
                first_line = False
                continue

            date.append(row[1])
            count.append(row[0])

            #print date

    return date, count

def main():
    date, count = import_data()
    temp = pd.Series(date)
    new_dates = pd.to_datetime(temp)

    print new_dates

    #plt.plot(new_dates, count)
    #plt.show()

if __name__ == '__main__':
    main()

'''
df = pd.read_csv('/home/schuyler/Desktop/Honors_Thesis/data_sets/date_counts.csv')

plt.plot_date(x=df['Date'], y=df['Count'])
plt.show()
'''
