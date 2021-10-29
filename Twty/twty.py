# TWTY - TWITTER COMMAND LINE INTERFACE TOOL
#
# CLI supports the following methods:
#   - List 'followers' and 'following' of given user
#   - Tweet
#   - Delete Tweets
#   - Follow and Unfollow users
#   - Filter (Delete) tweets based on specific words (don't get cancelled for past offensive tweets)
#   - Change Bio
#
#
# by 2021 Devarshi Patel <devarshi.patel@ryerson.ca>, Toronto
# Released under (C) WTFPL License
# -----------------------------------------------------------

import tweepy
import click

# library versions

print(f'tweepy version: {tweepy.__version__}\nclick version: {click.__version__}\n')

# tweepy authentication tokens, add your own from 

consumer_key = 'TektK3MCQB3mQ11adZmG2KeDK'
consumer_secret = 'KUZJ0VwahufHOSIgqMWil8A01MnbpUh2j9dmeUXd9XQyMSexVx'
access_token = '1295760434465775616-mg89HKYoVVcyhGSdcsBdO7z61mPfCh'
access_token_secret = 'jR02pfw8cS36wRY42fjS8kw3QexuTXYNDsRUzCEtATDs7'

# Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
MY_USERNAME = 'thefirstdev'


@click.group()
def cli():
    """TWITTER CLI"""
    pass


# GET FOLLOWERS -> twty showfollowers -user='user_name'

@cli.command()
@click.option('-user', default=MY_USERNAME, help='list of followers')
def showFollowers(user):
    print(f'followers of {user}:')
    for friend in api.get_followers(screen_name=user):
        print(friend.screen_name)


# GET FOLLOWING -> twty showfollowing -user='user_name'

@cli.command()
@click.option('-user', default=MY_USERNAME, help='list of following')
def showFollowing(user):
    print(f'{user} follows:')
    for friend in api.get_friends(screen_name=user):
        print(friend.screen_name)


# TWEET -> twty twt -t 'something'

@cli.command()
@click.option('-t', default='still thinking 💭', help='string to tweet')
def twt(t):
    api.update_status(t)
    print('✅ Successfully tweeted!')


# DELETE TWEETS -> twty dlt

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


# FOLLOW -> twty flw -user='user_name'

@cli.command()
@click.option('-user', help='username to follow')
def flw(user):
    try:
        api.create_friendship(screen_name=user)
        print(f'✅ Successfully followed {user}!')
    except Exception as e:
        print(f'{user} isn\'t an existing username')


# UNFOLLOW -> twty unflw -user='user_name'

@cli.command()
@click.option('-user', help='username to unfollow')
def unflw(user):
    for friend in tweepy.Cursor(api.get_friends).items():
        if friend.screen_name == user:
            api.destroy_friendship(screen_name=friend.screen_name)
            print(f'✅ Successfully unfollowed {user}!')


# CLEAN UP TWEETS -> twty cleanup -word='fag'

@cli.command()
@click.option('-word', help='username to unfollow')
def cleanup(word):
    for status in tweepy.Cursor(api.user_timeline, screen_name=MY_USERNAME, tweet_mode="extended").items():
        if word in status.full_text:
            print(f"\n>>>>> '{word}' was found in the following tweet:\n\t{status.full_text}")
            promptDelete = str(input('Would you like to delete this tweet? (y-yes/ n-no/ other-quit): '))

            if promptDelete.lower() == 'y':
                print('\t--deleted tweet')
                api.destroy_status(status.id)
            elif promptDelete.lower() == 'n':
                print('\t--untouched')
            else:
                print('\tquitting.')
                break
    print('✅ Done!\n')


# CHANGE BIO - twty bio -new='new_bio'

@cli.command()
@click.option('-new', default='', help='update your bio')
def bio(new):
    print(f'Your current bio: {api.get_user(screen_name=MY_USERNAME).description}')
    api.update_profile(description=new)
    print(f'✅ Successfully updated your bio.')


if __name__ == '__main__':
    cli()
