#!/usr/bin/python
import sys
import os
import json
import tweepy
import datetime
import re

auth = tweepy.OAuthHandler('lW1lQkWiSV86ROytPEabdBplB', 'cWUzxdgL2zJokUPRP1Msos00u1HhgI7bp33aLvJ4IkrhbsFjp6') #(consumer_key, consumer_secret)
auth.set_access_token('1184759057078521856-TYMiapY06vE5cfuhKOOlkeOmWKRMH8', 'BkD0wZcJJYRSg0thaDc7DqW2Cl8NdWtILyGnuJlglWyHy') #(access_token, access_token_secret)
api = tweepy.API(auth)

# Global variables
TODAY_DATE = 19 # Update this with every new day of month of March
NUM_TWEETS = 100

# Text Cleaning Function
def cleanTweet(string):
    # Given a String, Returns a Bag of Words (All Lowercase)
    # Removes:
    # - URLs
    # - NLTK Stop Words
    # - Twitter Specific Text: @ and RT
    words = string.lower().strip().split()
    for word in words:
        word = word.rstrip().lstrip()
        
        if re.match(r'^https?:\/\/.*[\r\n]*', word) \
        or re.match('\s', word) \
        or word == 'rt' or word == '':
            words.remove(word)

    return ' '.join(words) # Currently Returns a List of Words

# Make Sure Folder Exists
if not os.path.exists('data'):
    os.makedirs('data')

# Read through list of athletes
with open("athletes.json", "r") as f:
    athlete_dictionary = json.loads(f.read())

# For every athlete...
for key in athlete_dictionary:
    for i in range(7): # Search API only allows for 7 day intervals into past, not 20 as was originally believed
        file_name = 'data/' + key
        start_str = "2020-03-" + str(TODAY_DATE-(i+1))
        until_str = "2020-03-" + str(TODAY_DATE-i)
        file_name += "_" + start_str + ".txt"
        file = open(file_name, "wb+")

        # Search tweets within each day
        tweets = api.search(q=athlete_dictionary[key], count=NUM_TWEETS, since=start_str, until=until_str, tweet_mode="extended")

        # Get full text for both regular and retweeted tweets
        for tweet in tweets:
            if "retweeted_status" in dir(tweet):
                tweet = tweet.retweeted_status.full_text
            else:
                tweet = tweet.full_text

            if "https" in tweet:
                continue
            
            # replace newline to make sure that we only have one tweet per line
            tweet = tweet.replace('\n', ' ')
            tweet = cleanTweet(tweet)

            # Open new file and write
            file.write((tweet + "\n").encode('utf-8'))
