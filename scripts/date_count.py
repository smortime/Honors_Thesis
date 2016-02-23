#Schuyler Mortimer Honors Thesis
import csv

def fix_date(bad):
    date_list = bad.split()

    try:
        if date_list[1] in ('May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'):
            year = '2015'
        else:
            year = '2016'
    except:
        return 'NA'

    return date_list[1] + " " + date_list[2] + ", " + year


def import_master(date_count):
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as f:
        reader = csv.reader(f)
        temp = list(reader)

        for row in temp:
            date = fix_date(row[2])
            if date not in date_count:
                date_count[date] = 1
            else:
                date_count[date] += 1

def write_to_csv(date_count):
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/date_counts.csv', 'wb') as dates:

        try:
            dates.truncate()
        except:
            pass

        writer = csv.writer(dates)
        writer.writerow(["Count", "Date"])

        for k, v in date_count.items():
            writer.writerow([v, k])

def main():
    date_count = {}
    import_master(date_count)

    for k, v in date_count.items():
        print v, k

    write_to_csv(date_count)

if __name__ == '__main__':
    main()
