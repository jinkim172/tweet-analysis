from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import download
from sys import stdin

def sentiment_scores(sentence): 
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    score = sentiment_dict['compound'] # will be a score between -1 and +1
    # convert score to the same scale as the original regression model
    score *= 2
    score += 2
    # Get score between 0 and 100
    score *= 25
    # now, score will be between 0 and +100, just like the original one
    return score

if __name__ == "__main__":
    if not download('vader_lexicon', download_dir='./'):
        raise IOError("Vader lexicon not downloaded.")
    for line in stdin:
        print(sentiment_scores(line.strip()))