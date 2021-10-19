import tweepy
print(tweepy.__version__)

consumer_key = '1234'
consumer_secret = '1234'
access_token = '1234'
access_token_secret = '1234'

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_name = 'twitter_username_without_@'
user = api.get_user(screen_name=user_name)


def catchTraitors(followers, following):
    traitors = []
    for person in following:
        if person not in followers:
            traitors.append(person)
    return traitors


if __name__ == '__main__':
    followers = []
    for friend in user.followers():
        followers.append(friend.screen_name)

    following = []
    for person in user.friends():
        following.append(person.screen_name)

    # if the array of traitors is empty, you have no traitors
    if not catchTraitors(followers, following):
        print('The coast is clear')
    else:
        print('AHA CAUGHT THE TRAITORS!')
        print(catchTraitors(followers, following))
