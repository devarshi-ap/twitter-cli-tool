# _TWTY_, a Twitter command line interface tool
<br>

## Twty
(I'd recommend using this with a python venv as to avoid any furthur issues. Plus, it's the general practice anyways so might as well.)

Follow these steps to get started:

1. **_Get Personal API keys_**
    1. Go to [Twitter Developer Portal](https://developer.twitter.com/en)
    2. Signup with your Twitter Account
    3. Fill out mandatory form for developers
    4. Create Project/App
    5. Go to 'Project & Apps' under Dashboard
    6. Go to 'Keys & Tokens'
    7. Change the 'Access token & secrets' permission to 'read, write, and direct messages'
    8. **Save all 'API Keys & Secrets', 'Bearer Tokens', and 'Access Tokens & Secrets' somewhere safe and private.**
<br>

3. **_Clone this Repo_**
    - clone the repo like so:
    ```
    $ cd <wherever you wanna setup the project>
    $ git clone https://github.com/devarshi-ap/twitter-cli-tool.git
    ```
    - If you don't have [Git VCS](https://git-scm.com) installed, then just manually copy and paste the setup.py and twty.py file contents into ur IDE.
<br>

4. **_Install Dependencies_**
    - This project's dependencies incude: [_tweepy_](https://www.tweepy.org), [_click_](https://click.palletsprojects.com/en/8.0.x/), and _editables_.
    - Go to the project dir, and open the terminal and install the dependencies via:
    ```
    $ pip install tweepy
    $ pip install click
    $ pip install --editables .
    ```
<br>

5. **_Edit Authentication Values_**
    - In twty.py, replace the values for the _consumer_key_, _consumer_secret_, _access_token_, and _access_token_secret_ with your values from the Twitter developer portal.
    - Also, replace the _MY_USERNAME_ variable with your twitter handle (ie. MY_USERNAME='elonmusk')
<br>

NOTE: Alright, Imma be real with you, I'm not sure if the following terminal command is needed to be called, but just run it to be sure. (not the file path of twty.py or setup.py; the path of the folder they're both inside): ```$ pip install -e <project folder path>```

<br>

---
## FollowsBack.py
After reading the above instructions, After setting up with your own credentials and usernames and what not, just run the file in the terminal with:
```
$ python followsBack.py
```
This should print out a list of traitors whom you follow but don't follow you back.

---

<br>

P.S.
    
    1. If your confused as to how cli options and arguments work and are used, so that you may use the one's I've made, then you know... google it.
    
    2. I've also provided pretty semantic-fill-in-the-blank variable values for you to fill out for your values (ie. ur API credentials and YOUR twitter username).

    3. I've also commented, above the methods, after the '->'s, the actual commands you can run in the terminal.

    4. If you run into any problems, my contact info is on my site linked on my profile.
    
    5. Suprisingly, when you use the tweepy library, you actually don't bite into your monthly rate limit for the actual Twitter API.)
