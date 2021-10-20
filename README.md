# tweepy-projects
projects made using the tweepy library (python wrapper for twitter api)

----

## FollowsBack.py
Read the below prerequisite note for context. After setting up with your own credentials and usernames and what not, just run the file in the terminal with:
- $ python followsBack.py
This should print out a list of traitors whom you follow but don't follow you back.

----

## Twitter-Cli.py
I'd recommend using this with a python venv as to avoid any furthur issues. Plus, it's the general practice anyways so might as well.

Prerequisite setup to the actual setup:
- You're going to need your own Twitter Developer's API Keys and Secret credentials to use their api endpoints. Suprisingly, when you use the tweepy library, you actually don't bite into your monthly rate limit for the actual Twitter API. This is likely because we aren't directly calling it; we are using a python wrapper library (tweepy) for the actual Twitter API.

1. Set up Virtual Environment (optional)
- $ pip install virtualenv --user

- Then go into this project folder and set up the venv
- $ virtual venv

- Now activate the venv
- $ . venv/bin/activate

To quit the venv, use:
- $ deactivate

2. Install Dependencies
- $ pip install tweepy
- $ pip install click

And your set!

P.S.
    
    1. If your confused as to how cli options and arguments work and are used, so that you may use the one's I've made, then you know... google it.
    
    2. I've also provided pretty semantic-fill-in-the-blank variable values for you to fill out for your values (ie. ur API credentials and YOUR twitter username).

    3. I've also commented, above the methods, after the '->'s, the actual commands you can run in the terminal.

    4. If you run into any problems, my contact info is on my site linked on my profile.
