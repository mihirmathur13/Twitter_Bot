import tweepy
import tkinter as tk

# API Key
# ********************

# API Key Secret
# ******************************

# Access Token
# **************************************************

# Access Token Secret
# ********************************

consumer_key = '********************'
consumer_secret = '******************************'
access_token = '**************************************************'
access_token_secret = '********************************'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# user = api.verify_credentials()  # Use this instead of api.me()
# if user:
#     print("Authenticated as:", user.name)
# else:
#     print("Authentication failed!")



def mainFunction():
    # for follower in tweepy.Cursor(api.get_followers).items():
    #     try:
    #         follower.follow()
    #         print ("Followed everyone that is following " + user.name)
    #     except tweepy.TweepyException as e:
    #         print(e.reason)
    #     except StopIteration:
    #         break
        
    search = "trump"
    numberOfTweets = 10
    for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print('Retweeted the tweet')
        except tweepy.TweepyException as e:
            print(e.reason)
        except StopIteration:
            break
    
    phrase = "Reply message"
    for tweet in tweepy.Cursor(api.search_tweets, q=search, lang="en").items(numberOfTweets):
        try:
            tweetId= tweet.id
            username = tweet.user.screen_name
            api.update_status(f"@{username} {phrase}", in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)
            print(f"Replied to @{username} with: {phrase}")
        except tweepy.TweepyException as e:
            print(e.reason)
        except StopIteration:
            break
        
mainFunction()
