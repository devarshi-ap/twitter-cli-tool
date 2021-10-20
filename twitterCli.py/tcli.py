# TWITTER COMMAND LINE INTERFACE TOOL
#
# CLI supports the following methods:
#   - List 'followers' and 'following' of given user
#   - Tweet
#   - Delete Tweets
#   - Follow and Unfollow users
#   - Filter (Delete) tweets based on specific words (don't get cancelled for past offensive tweets)
#
#
# by 2021 Devarshi Patel <devarshi.patel@ryerson.ca>, Toronto
# Released under (C) WTFPL License
# -----------------------------------------------------------

import tweepy
import click

# library versions

print(f'tweepy version: {tweepy.__version__}\nclick version: {click.__version__}\n')

# tweepy authentication tokens

consumer_key = 'xxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxx'

# Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
MY_USERNAME = 'your_username_here_without_@'