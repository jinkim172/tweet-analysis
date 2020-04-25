# Install GetOldTweets3 with 'pip3 install GetOldTweets3'

import sys
import os
import json
import GetOldTweets3 as got
import datetime as dt
import re

# Global variables
TODAY_DATE = 19 # Update this with every new day of month of March
START_DATE = dt.datetime(2020, 2, 1) # 2020-02-01 
END_DATE = dt.datetime(2020, 2, 5) # 2020-02-05 
MAX_TWEETS_PER_DAY = 100 

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
if not os.path.exists('old_data'):
    os.makedirs('old_data')

# Read through list of athletes
with open("athletes_test.json", "r") as f:
    athlete_dictionary = json.loads(f.read())

# For Every Day in Range
while START_DATE != END_DATE:
    
    # Calculate Current Day
    START = str(START_DATE.date())
    END = str((START_DATE + dt.timedelta(days=1)).date())

    # For every athlete...
    for key in athlete_dictionary:
        # Print Progress
        print(f'Processing {key} on {START_DATE.date()}...')

        # Retreive Tweets For Given Parameters
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(athlete_dictionary[key])\
                                                .setSince(START)\
                                                .setUntil(END)\
                                                .setMaxTweets(MAX_TWEETS_PER_DAY)

        curr_tweets = [t.text for t in got.manager.TweetManager.getTweets(tweetCriteria)]

        # Write Data to Files
        file_name = 'old_data/' + key + '_' + START + '.txt'
        file = open(file_name, "wb+")

        # Open new file and write
        file.write(('\n'.join(curr_tweets).encode('utf-8')))

    # Increment Day
    START_DATE += dt.timedelta(days=1)