#Schuyler Mortimer Honors Thesis
#Probably will not be needing this script
import csv

with open("/home/schuyler/Desktop/test1.csv", "rb") as data:

    reader = csv.reader(data)
    temp = list(reader)
    count = 1
    first_line = False

    for row in temp:

        if first_line:
            first_line = False
            continue

        text_file = open("/home/schuyler/Desktop/test_model/" + str(count) + ".txt", "w")
        text_file.write(row[1])
        text_file.close()
        count += 1
