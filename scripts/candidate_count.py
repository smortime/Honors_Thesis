#Schuyler Mortimer Honors Thesis
import csv

def count_candidate(path):
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        temp = list(reader)

        tweet_count = {}

        for row in temp:
            if row[0] not in tweet_count:
                tweet_count[row[0]] = 1
            else:
                tweet_count[row[0]] += 1

        return tweet_count

def write_csv(tweet_count):
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/candidates_twitter.csv', 'rb') as f:
        reader = csv.reader(f)
        temp = list(reader)

        new_count = {}
        
        for row in temp:
            for key, value in tweet_count.iteritems():
                if row[0] == key:
                    new_count[row[0]] = value
                    continue

        for k, v in new_count.iteritems():
            print k, v

    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/tweet_count.csv', 'wb') as w:
        writer = csv.writer(w)
        writer.writerow(['Candidate', 'Count'])

        for key, value in new_count.iteritems():
            writer.writerow([key, value])


def main():
    path = raw_input("File path: ")
    tweet_count = count_candidate(path)
    write_csv(tweet_count)


if __name__ == '__main__':
    main()
