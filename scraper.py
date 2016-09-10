import tweepy
from tweepy import OAuthHandler

consumer_key = 
consumer_secret = 
access_token = 
access_secret = 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

print("Please input your Twitter Target")
twitterid = str(input())
print("Please input your target file")
txt = open(str(input()),'w')
print("How many tweets do you need from timeline? (Max 3200)")
num = int(input())


for status in tweepy.Cursor(api.user_timeline, twitterid).items(num):
    txt.write(status.text)
    txt.write("\n")
