import tweepy
from keys import *

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_level_secret')

twitter_api = tweepy.API('auth')

cfg_tweets = twitter_api.search(
	q="CodeFirstGirls"
)

for tweet in cfg_tweets:
	print tweet.user.name + ": " + tweet.text












