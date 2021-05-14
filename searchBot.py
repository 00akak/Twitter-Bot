import tweepy
import time

consumer_key='#your api-key'
consumer_secret='your api scereat key'
key='your token'
secret='your screat token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)

hashtag="python"
tweetNumber=3
tweets=tweepy.Cursor(api.search, hashtag).items(tweetNumber)
def searchBot():

 for tweet in tweets:
    try:    
     tweet.retweet()
     print("retweet done...")
     time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
searchBot()        


