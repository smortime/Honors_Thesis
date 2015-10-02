#Schuyler Mortimer Honors Thesis
import csv
import numpy as np
import time
import json
from twython import Twython

#Removes special characters from tweet text
def Remove_Character(character, text):
    new_text = text.replace(character, "")
    return new_text

#Setting up the Twitter API requirements / Twython
APP_KEY = "Insert APP_KEY here"
APP_SECRET = "Insert APP_SECRET here"
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

#Prepping candidates' twitter users from csv file
candidates_file = open("candidates_twitter.csv", "rb")
candidates_reader = csv.reader(candidates_file)

#Storing the user names in a list
candidates_list = []
for candidate in candidates_reader:
    candidates_list.append(candidate)

row_count = len(candidates_list)

#Number of tweets you want to pull PER candidate
tweet_count = 200

print "twitter_pull.py is running..."

#Iterate through the candidates and pull their most recent 200 tweets
#Writes tweet, date, favorites, and retweets to a csv
with open("test.csv", "wb") as tweets:

    #Add header
    writer = csv.writer(tweets)
    writer.writerow(["user_name", "tweet_body", "date", "favorite_count", "retweet_count", "retweeted", "source"])

    for i in range(0,row_count):

        #pull out just the candidate's name
        user = str(candidates_list[i])[2:-2]

        print "Pulling "+user+"'s timeline"

        #Lookup the candidate's timeline
        try:
            search = twitter.get_user_timeline(screen_name = user, count=tweet_count)
        except:
            search = 'null'

        #Checking if valid twitter account was pulled
        if search == 'null':
            pass
        else:
            writer = csv.writer(tweets)

        #Pulls specific parts of the candidate's timeline
        for j in range(0,tweet_count):
            try:
                text = search[j] ['text']

                #Checks for semicolon / removes from string if it contains one
                if(";" in text):
                    text = Remove_Character(";", text)

            except IndexError:
                text = 'null'

            try:
                time = search[j] ['created_at']
            except IndexError:
                time = 'null'

            try:
                favorite = str(search[j] ['favorite_count'])
            except IndexError:
                favorite = 'null'

            try:
                retweet = str(search[j] ['retweet_count'])
            except IndexError:
                retweet = 'null'

            try:
                retweeted = str(search[j] ['retweeted'])
            except IndexError:
                retweeted = 'null'

            try:
                source = search[j] ['source']
            except IndexError:
                source = 'null'

            user_name = ['user']

            #Writing the user timeline to the a .csv
            row_data = [[user.encode("utf-8")]+[text.encode("utf-8")]+[time.encode("utf-8")]+
            [favorite.encode("utf-8")]+[retweet.encode("utf-8")]+[retweeted.encode("utf-8")]+[source.encode("utf-8")]]

            array = np.array(row_data)
            for data in array:
                writer.writerow(data)

print "twitter_pull.py is complete"
