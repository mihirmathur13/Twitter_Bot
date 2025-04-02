import tweepy
import tkinter as tk

# API Key

# AS2c3h8yYDtz1HaIIACu3WIg6

# API Key Secret

# LV8rkXyEuof4fAp6RJmJVdUDoxH7xRyOrZ40U8CXvYPQ3ksb6b

# Access Token

# 1903903877172494336-OSROldEGq1lRwcaUaeGXPrxua3r1Aa

# Access Token Secret

# ye4zKMPASxjsm9zxLI0yiJeS65nCNUAidr6kss4LRj539

consumer_key = 'AS2c3h8yYDtz1HaIIACu3WIg6'
consumer_secret = 'LV8rkXyEuof4fAp6RJmJVdUDoxH7xRyOrZ40U8CXvYPQ3ksb6b'
access_token = '1903903877172494336-OSROldEGq1lRwcaUaeGXPrxua3r1Aa'
access_token_secret = 'ye4zKMPASxjsm9zxLI0yiJeS65nCNUAidr6kss4LRj539'

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