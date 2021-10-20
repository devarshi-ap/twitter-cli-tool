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


@click.group()
def cli():
    """TWITTER CLI"""
    pass


# GET FOLLOWERS -> python3 tcli.py showfollowers -user='user_name'

@cli.command()
@click.option('-user', default=MY_USERNAME, help='list of followers')
def showFollowers(user):
    for friend in api.get_followers(screen_name=user):
        print(friend.screen_name)


# GET FOLLOWING -> python3 tcli.py showfollowing -user='user_name'

@cli.command()
@click.option('-user', default=MY_USERNAME, help='list of following')
def showFollowing(user):
    for friend in api.get_friends(screen_name=user):
        print(friend.screen_name)


# TWEET -> python3 tcli.py twt -t 'something'

@cli.command()
@click.option('-t', default='still thinking 💭', help='string to tweet')
def twt(t):
    api.update_status(t)
    print('✅ Successfully tweeted!')


# DELETE TWEETS -> python3 tcli.py dlt

@cli.command()
def dlt():
    for status in tweepy.Cursor(api.user_timeline, screen_name=MY_USERNAME, tweet_mode="extended").items():
        print(f'\n>>>>> "{status.full_text}"')
        promptDelete = str(input('\tDelete? (y/n/q-quit): '))

        if promptDelete.lower() == 'y':
            print('\t--deleted tweet')
            api.destroy_status(status.id)
        elif promptDelete.lower() == 'n':
            print('\t--untouched')
        else:
            print('\tquitting.')
            break
    print('✅ Done!\n')


# FOLLOW -> python3 tcli.py flw -user='user_name'

@cli.command()
@click.option('-user', help='username to follow')
def flw(user):
    try:
        api.create_friendship(screen_name=user)
        print(f'✅ Successfully followed {user}!')
    except Exception as e:
        print(f'{user} isn\'t an existing username')


# UNFOLLOW - python3 tcli.py unflw -user='user_name'

@cli.command()
@click.option('-user', help='username to unfollow')
def unflw(user):
    for friend in tweepy.Cursor(api.get_friends).items():
        if friend.screen_name == user:
            api.destroy_friendship(screen_name=friend.screen_name)
            print(f'✅ Successfully unfollowed {user}!')