# get_tweets.py
# Allen Duong (aduong1), Jin Kim (jkim56), Nicholas Marcopoli (nmarcopo)
# Description:

import tweepy
import json

auth = tweepy.OAuthHandler('lW1lQkWiSV86ROytPEabdBplB', 'cWUzxdgL2zJokUPRP1Msos00u1HhgI7bp33aLvJ4IkrhbsFjp6') #(consumer_key, consumer_secret)
auth.set_access_token('1184759057078521856-TYMiapY06vE5cfuhKOOlkeOmWKRMH8', 'BkD0wZcJJYRSg0thaDc7DqW2Cl8NdWtILyGnuJlglWyHy') #(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
        if self.num_tweets < 5:
            text = status.text
            with open("output.txt", "a", encoding='utf-8') as f:
                f.write(status.text + "\r\n\n")
            print(text)
            self.num_tweets += 1
            return True
        else:
            return False

    def on_error(self, status):
        print ('Error on status', status)
        if status == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_limit(self, status):
        print ('Limit threshold exceeded'), status

    def on_timeout(self, status):
        print ('Stream disconnected; continuing...')

#if __name__ == "__main__":

with open("people2.json", "r") as f:
    athlete_dictionary = json.loads(f.read())

for key in athlete_dictionary:
    tracker = athlete_dictionary[key]
    stream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
    stream.filter(track=tracker)
