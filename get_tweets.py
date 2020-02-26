# get_tweets.py
# Allen Duong (aduong1), Jin Kim (jkim56), Nicholas Marcopoli (nmarcopo)
# Description: 

import tweepy
import json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
            if self.num_tweets < 2:
                text = status.text
                # g.write(text + "\r\n\n")
                with open("out.csv", "a", encoding='utf-8') as f:
                    f.write("%s\n" % (status.text))
                print(text)
                self.num_tweets += 1
                return True
            else:
                return False

    def on_error(self, status):
        print ('Error on status', status)

    def on_limit(self, status):
        print ('Limit threshold exceeded'), status

    def on_timeout(self, status):
        print ('Stream disconnected; continuing...')

if __name__ == "__main__":
    auth = tweepy.OAuthHandler('lW1lQkWiSV86ROytPEabdBplB', 'cWUzxdgL2zJokUPRP1Msos00u1HhgI7bp33aLvJ4IkrhbsFjp6') #(consumer_key, consumer_secret)
    auth.set_access_token('1184759057078521856-TYMiapY06vE5cfuhKOOlkeOmWKRMH8', 'BkD0wZcJJYRSg0thaDc7DqW2Cl8NdWtILyGnuJlglWyHy') #(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
    
    # g = open("tweets_storage.txt", "w", encoding='utf-8')
    
    # key - athlete name, value = {"handle": "@lebronjames", "affiliation": "NBA", "hashtags": ["#lebronjames", "#kingjames"]}
    with open("people.json", "r") as f:
        DICTIONARY_NAME = json.loads(f.read())

    for key in DICTIONARY_NAME:
        tracker=[]
        tracker.append(DICTIONARY_NAME[key]["twitter_handle"])
        for hashtag in DICTIONARY_NAME[key]["hashtags"]:
            tracker.append(hashtag)
        stream.filter(track=tracker)