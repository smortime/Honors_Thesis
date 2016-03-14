#Schuyler Mortimer Honors Thesis
import csv

def add_master():
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as f:

        reader = csv.reader(f)
        temp = list(reader)
        date = []
        text = []

        for row in temp:
            date.append(row[2])
            text.append(row[1])

        return date, text

def add_new_data(text, date):

    #insert the file names that need to be added
    files = ['''Up through 19 added''']

    for f in files:
        file_name = "/home/schuyler/Desktop/Honors_Thesis/data_sets/twitter_pulls/" + f
        with open(file_name, 'rb') as f, open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'a') as m:

            reader = csv.reader(f)
            writer = csv.writer(m)
            temp = list(reader)

            for row in temp:
                if row[1] not in text and row[2] not in date:
                    writer.writerow(row)
                    text.append(row[1])
                    date.append(row[2])
                    print row
                elif row[1] not in text:
                    text.append(row[1])
                    print row

def main():
    print "[+] Running merge_data.py \n"
    date, text = add_master()
    add_new_data(text, date)
    print "\n[+] merge_data.py is complete"

if __name__ == '__main__':
    main()
