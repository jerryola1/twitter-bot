from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

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

client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token', client_id=client_id, client_secret=client_secret)


# authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# create an API object
api = tweepy.API(auth)

# # write a function to get the user's timeline
# def get_timeline():
#     # get the user's timeline
#     timeline = api.home_timeline()
#     # iterate over the tweets
#     for tweet in timeline:
#         # print the tweet's text
#         print(tweet.text)   

# write a function to post a tweet
def post_tweet():
    # get the user's input
    tweet = input('What would you like to tweet? ')
    # post the tweet
    api.update_status(tweet)
    print('Tweet posted!')

# call the function
post_tweet()