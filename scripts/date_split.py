#Schuyler Mortimer Honors Thesis
import csv

def get_dates():
    start = raw_input("Start date (Month Day): ")
    end = raw_input("End date: ")

    start_month, start_day = split_dates(start)
    end_month, end_day = split_dates(end)

    return start_month, start_day, end_month, end_day

def split_dates(date):
    list = date.split()
    day = int(list[1])
    return list[0], day

def split_csv_dates(date):
    list = date.split()
    day = int(list[2])
    return list[1], day

def main():

    start_month, start_day, end_month, end_day = get_dates()
    file_name = '/home/schuyler/Desktop/Honors_Thesis/data_sets/model_data/' + start_month + str(start_day) + '.csv'


    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as master, open(file_name, 'wb') as test:
        reader = csv.reader(master)
        writer = csv.writer(test)

        temp = list(reader)

        first_line = True

        writer.writerow(["user_name", "tweet_body", "date", "favorite_count", "retweet_count", "retweeted", "source"])

        for row in temp:

            if first_line:
                first_line = False
                continue

            try:
                temp_month, temp_date = split_csv_dates(row[2])

            except:
                continue

            if(temp_month == start_month and temp_date >= start_day):
                writer.writerow(row)
                print temp_month
                print temp_date

            elif(temp_month == end_month and temp_date <= end_day):
                writer.writerow(row)
                print temp_month
                print temp_date

if __name__ == '__main__':
    main()
