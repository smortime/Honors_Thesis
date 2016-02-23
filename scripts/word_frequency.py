#Schuyler Mortimer Honors Thesis
from nltk.corpus import stopwords
import csv

def import_words(file_path):
    with open(file_path, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)

        text = []

        for tweet in data:
            temp = tweet[1].split()
            for word in temp:
                text.append(word)

        return text

def remove_stop(words):
    filtered_words = [word for word in words if word not in stopwords.words('english')]
    return filtered_words

def word_count(filtered_words):
    count = {}

    for word in filtered_words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count


def main():
    words = import_words('/home/schuyler/Desktop/Honors_Thesis/data_sets/master.csv')
    filtered = remove_stop(words)
    count = word_count(filtered)

    for v, k in count:
        print v, k

if __name__ == "__main__":
    main()
