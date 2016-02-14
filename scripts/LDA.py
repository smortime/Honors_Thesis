#Schuyler Mortimer Honors Thesis
#WORK IN PROGRESS....
import csv
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words

def remove_stop_words(tokens):
    en_stop = get_stop_words('en')

    stopped_tokens = []

'''
    for token in tokens:
        for i in token:
            if i not in en_stop:
                stopped_tokens.append(i)
'''

    stopped_tokens = [ i for i in tokens if not i in en_stop]

    print stopped_tokens

def tokenize_txt_files(txt_list):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = []


    for tweet in txt_list:
        temp = tweet.lower()
        token = tokenizer.tokenize(temp)
        tokens.append(token)

        print tokens

def import_txt(file_name):

    with open(file_name, "rb") as data:

        reader = csv.reader(data)
        temp = list(reader)

        txt_set = []
        first_line = True

        for row in temp:
            if first_line:
                first_line = False
                continue

            txt_set.append(row[1])

        return txt_set

'''
    txt_set = []
    i = 1

    while(i < 10000):

        try:
            temp = open("/home/schuyler/Desktop/test_model/" + i, "w")
        except:
            continue

        text_set.append
'''

def main():
    txt_set = import_txt("/home/schuyler/Desktop/test1.csv")
    tokens = tokenize_txt_files(txt_set)
    #remove_stop_words(tokens)
    #print txt_set

if __name__ == '__main__':
    main()
