import RPi.GPIO as GPIO
import time
import tweepy
import csv


def twitter_thread(consumer_key, consumer_secret, access_key, access_secret):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(19,GPIO.OUT)

    tweet_data1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    tweet_data2=[]

    while True:
        for tweet in tweepy.Cursor(api.user_timeline,id = "StackOverflow",exclude_replies = True).items(10):
                tweet_data2.append([tweet.id,tweet.favorite_count,tweet.retweet_count,tweet.text])
        for i in range(10):
            for j in range(10):
                if tweet_data2[j][0] == tweet_data1[i][0] and tweet_data2[j][1] > tweet_data1[i][1]:
                    print(tweet_data2[j][3],'\nOne more favorite')
                    GPIO.output(19,GPIO.HIGH)
                    time.sleep(20)
                    print ("LED off")
                    GPIO.output(19,GPIO.LOW)
        tweet_data1 = tweet_data2 
        tweet_data2 = []          
        time.sleep(60)
