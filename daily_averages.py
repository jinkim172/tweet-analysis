# Print Average Sentiment Scores, Per Day, Per Player
import subprocess
import os
import json
from tqdm import tqdm

# Prints Sentiment Score Per Player Each Day
def average_daily_per_player():
    # Initialize Variables
    average_scores = {}

    entries = list(os.scandir('./old_data/'))
    for entry in tqdm(entries, total=len(entries)): 

        # Parse Entry Filename
        player, date = entry.path[7:-4].split('_')
        
        # Calculate Sentiment Score For File
        input = '\n'.join([tweet for tweet in open(entry, 'r')]).encode('utf-8')
        res = subprocess.run(['python3', 'get_sentiment.py'],  cwd="./regression", stdout=subprocess.PIPE, input=input).stdout.decode('utf-8')
        res = [float(i) for i in res.split('\n') if len(i) > 0]

        # Check For Empty List
        if len(res) < 1:
            continue

        # Add Average Score to Dictionary
        avg = sum(res)/len(res)
        if date not in average_scores.keys():
            average_scores[date] = {}
        average_scores[date][player] = avg

    # Print Output
    return average_scores

# Main Execution
if __name__ == "__main__":
    # Get Daily Averages
    results = average_daily_per_player()

    # Print Results
    for date in results.keys():
        print('DATE:', date)

        for player in results[date]:
            print('\t-', player, results[date][player])


