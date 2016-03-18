#Schuyler Mortimer Honors Thesis
import csv

term = {}

with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as data:
    reader = csv.reader(data)

    for row in reader:
        temp = row[1].split()
        for word in temp:
            if word not in term:
                term[word] = 1
            else:
                term[word] +=1


for k, v in term.iteritems():
    print k, v

with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/term_frequency.csv', 'wb') as new:
    writer = csv.writer(new)
    writer.writerow(['Term','Count'])

    for k, v in term.iteritems():
        writer.writerow([k,v])
