import tweepy
import os
from keys import *

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_level_secret')

twitter_api = tweepy.API('auth')

cfg_tweets = twitter_api.search(
	q="CodeFirstGirls"
)

for tweet in cfg_tweets:
	print tweet.user.name + ": " + tweet.text

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)












