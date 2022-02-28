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
    $ pip install tweepy click python-dotenv
    ```
<br>

5. **_Edit Authentication Values_**
    - Create a .env file and add your Twitter developer credentials:
    ```txt
        CONSUMER_KEY = "add"
        CONSUMER_SECRET = "your"
        ACCESS_TOKEN = "credentials"
        ACCESS_TOKEN_SECRET = "here"
        MY_USERNAME = "and your twitter handle here" 
    ```
<br>

<br>

---
## FollowsBack.py
After having set up your twitter api keys in the dotenv, to use this program, just run the file in the terminal:
```
$ python followsBack.py
```
This should print out a list of traitors whom you follow but don't follow you back.

---

<br>

P.S.
    
    1. If your confused as to how cli options and arguments work and are used, so that you may use the one's I've made, then you know... google it.

    2. I've also commented, above the methods, after the '->'s, the actual commands you can run in the terminal.

    3. If you run into any problems, my contact info is on my site linked on my profile.
    
    4. Suprisingly, when you use the tweepy library, you actually don't bite into your monthly rate limit for the actual Twitter API.
