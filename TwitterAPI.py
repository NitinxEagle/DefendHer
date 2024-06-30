import tweepy
import json

# Twitter API v2 credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKRaugEAAAAA%2FmAlvCouy%2FgmYgFQK%2FFOGEpze3w%3DgczBxQ8vH9e9aPLSkEGG2JvS8XWmt8MWQwydhGn7A09tY7c3r8"

# Authenticate with the Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Define query and parameters
query = "safety"
max_results = 100  # Number of tweets to fetch

try:
    # Collect tweets
    tweets = client.search_recent_tweets(query=query, max_results=max_results)

    # Save tweets to a JSON file
    with open('tweets_v2.json', 'w') as f:
        for tweet in tweets.data:
            f.write(json.dumps(tweet.data) + "\n")

    print("Tweets fetched successfully!")

except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")
