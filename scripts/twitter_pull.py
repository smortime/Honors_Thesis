#Schuyler Mortimer Honors Thesis
import csv
import numpy as np
from twython import Twython
import shelve

#Removes special characters from tweet text
def remove_character(character, text):
    new_text = text.replace(character, "")
    return new_text

#Setting up the Twitter API requirements / Twython
APP_KEY = "APP_KEY HERE"
APP_SECRET = "APP_SECRET HERE"
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

#Prepping candidates' twitter handles from csv file
candidate_file = open('/home/schuyler/Desktop/Honors_Thesis/data_sets/candidates_twitter.csv', "rb")
candidates_reader = csv.reader(candidate_file)

candidates_list = []
for candidate in candidates_reader:
    candidates_list.append(candidate)

row_count = len(candidates_list)

#Number of tweets you want to pull PER candidate
tweet_count = 200

#Auto naming file name everytime script is pulled
shelf_file = shelve.open('/home/schuyler/Desktop/Honors_Thesis/data_sets/file_version')
file_name = '/home/schuyler/Desktop/Honors_Thesis/data_sets/twitter_pulls/pull' + str(shelf_file['version']) + '.csv'
shelf_file['version'] = shelf_file['version'] + 1
shelf_file.close()

print "twitter_pull.py is running...\n"

#Iterate through the candidates and pull their most recent 200 tweets
#Writes tweet, date, favorites, and retweets to a csv
with open(file_name, "wb") as tweets:

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

        for j in range(0,tweet_count):
            try:
                text = search[j] ['text']

                #Checks for semicolon / removes from string if it contains one
                if(";" in text):
                    text = remove_character(";", text)

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

print "\ntwitter_pull.py is complete"
