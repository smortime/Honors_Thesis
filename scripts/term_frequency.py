#Schuyler Mortimer Honors Thesis
import csv
from string import punctuation
from nltk.corpus import stopwords

def import_words():
    with open('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv', 'rb') as data:
        reader = csv.reader(data)
        return_list = []

        for row in reader:
            temp = preprocess(row[1])

            for word in temp:
                return_list.append(word)

        return return_list

def preprocess(tweet):
    stop = stopwords.words('english')

    for p in list(punctuation):
        tweet = tweet.replace(p, '')

    processed_tweet = tweet.decode('utf-8').lower().split()

    processed_tweet = [i for i in processed_tweet if i not in stop]
    processed_tweet = [i for i in processed_tweet if i not in punctuation]
    return processed_tweet

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
