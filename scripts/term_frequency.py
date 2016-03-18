#Schuyler Mortimer Honors Thesis
import csv
from string import punctuation
from nltk.corpus import stopwords 

def import_words():
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as data:
        reader = csv.reader(data)
        return_list = []

        for row in reader:
            temp = preprocess(row[1]).split()
            for word in temp:
                return_list.append(word)

        return return_list

def preprocess(tweet):
    stop = stopwords.words('english')
    processed_tweet = tweet.decode('utf-8').lower()

    for p in list(punctuation):
        processed_tweet = processed_tweet.replace(p,'')

        return processed_tweet


    for w in stop:
        processed_tweet = processed_tweet.replace(" " + w + " ", '')


def frequency_count(text):
    term_frequency = {}

    for word in text:
        if word not in term_frequency:
            term_frequency[word] = 1
        else:
            term_frequency[word] += 1

    return term_frequency

def main():
    words = import_words()
    terms = frequency_count(words)

    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/term_frequency2.csv', 'wb') as new:
        writer = csv.writer(new)
        writer.writerow(['Term', 'Count'])

        for k, v in terms.iteritems():
            writer.writerow([k.encode('utf-8'),v])

if __name__ == '__main__':
    main()
