from dotenv import load_dotenv
import os
load_dotenv()  
client_id = os.getenv('TWITTER_CLIENT_ID')
client_secret = os.getenv('TWITTER_CLIENT_SECRET')

# import tweepy library
import tweepy
# set up authentication credentials
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# create an API object
api = tweepy.API(auth)

# write a function to post a tweet
def post_tweet():
    # get the user's input
    tweet = input('What would you like to tweet? ')
    # post the tweet
    api.update_status(tweet)
    print('Tweet posted!')

# call the function
post_tweet()