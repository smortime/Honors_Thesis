Scripts Overview
======
## 1. [create_shelf.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/create_shelf.py)
- **Purpose:** Sets up a shelve file so that [twitter_pull.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/twitter_pull.py) can add / keep track of the pull number to the output's file name. Starts at 3 because I pulled twice before implementing this feature.

## 2. [twitter_pull.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/twitter_pull.py)
- **Purpose:** This is script is used to make request to the [Twitter API](https://dev.twitter.com/rest/reference/get/statuses/user_timeline) for each of the candidates listed in the candidates_twitter.csv. It will then attempt to pull their twitter timeline and write their last 200 tweet's data (tweet, date, favorites, retweets, retweeted, and source) to pullx.csv.

## 3. [date_count.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/date_count.py)
- **Purpose:** Creates a csv with each date and the number of tweets for that day between all the candidates. These counts are mostly just for some exploratory reasons.

## 4. [date_split.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/date_split.py)
- **Purpose:** Creates a csv that contains only the tweets from the user defined period. The output csv from this script will generally be used in the models.

## 5. [candidate_count.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/candidate_count.py)
- **Purpose:** Returns candidates with how many tweets they have in master.csv.

## 6. [csv_to_text.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/csv_to_text.py)
- **Purpose:** Converts the tweet text column found in .csv files into individual text files per each tweet. LDA model requires the data to be in text files.

## 7. [merge_data.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/merge_data.py)
- **Purpose:** Takes in all the pullx.csv files and merges into master.csv, gets rid of the duplicate tweets.

## 8. [term_frequency.py](https://github.com/smortime/Honors_Thesis/blob/master/scripts/term_frequency.py)
- **Purpose:** Implementation of term frequency, counts the occurence of every word in tweet data set, with some minimal preprocessing.

## 9. [LDA.R](https://github.com/smortime/Honors_Thesis/blob/master/scripts/LDA.R)
- **Purpose:** The implementation of LDA model, the preprocessing is done within this script aswell. 

### Dependencies / Notes
- **_Python_:** All scripts were run using Python 2.7.6.
- **_R_** 
- **_Twython:_** All scripts that pull from the Twitter API require the [Twython library](https://github.com/ryanmcgrath/twython).
- **_Pandas / Numpy_** Some scripts will require [Pandas](http://pandas.pydata.org/) and [NumPy](http://www.numpy.org/).
