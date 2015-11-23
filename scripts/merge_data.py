#Schuyler Mortimer Honors Thesis
#NOT READY TO BE USED, STILL NEEDS MAJOR WORK
import csv

print "Running merge_data"

master_path = "/home/schuyler/Desktop/data_sets/master.csv"
new_path = raw_input("Path of file to add to master file: ")

with open(master_path, "rb") as master, open(new_path, "rb") as new:

    #reads the master file in a list of tuples
    try:
        next(master)
        data = [tuple(line) for line in csv.reader(master)]
    except:
        print "Nothing in file"

    #reads in the file to be added as a list of tuples
    try:
        next(new)
        new_data = [tuple(line) for line in csv.reader(new)]
    except:
        print "Something is wrong..."

    #Add the new file to the master list of tuples
    for tup in new_data:
        data.append(tup)

with open(master_path, "wb") as master:

    #clears master file for rewrite
    master.truncate()

    #writes the header
    writer = csv.writer(master)
    writer.writerow(["user_name", "tweet_body", "date", "favorite_count", "retweet_count", "retweeted", "source"])

    #writes all tuples to master file
    for row in data:
        writer.writerow(row)

print "merge_data complete"
