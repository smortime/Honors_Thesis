#Schuyler Mortimer Honors Thesis
#Probably will not be needing this script
import csv

#Change filepath to the month you want
with open("/home/schuyler/Documents/Honors_Thesis/data_sets/HICSS/Feb1.csv", "rb") as data:

    reader = csv.reader(data)
    temp = list(reader)
    count = 1
    first_line = False

    for row in temp:

        if first_line:
            first_line = False
            continue

        text_file = open("/home/schuyler/Documents/text_files/feb/" + str(count) + ".txt", "w")
        text_file.write(row[1])
        text_file.close()
        count += 1
