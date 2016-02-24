#!/usr/local/bin/python

#credits to http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#Peter Liang, a New York Police Department officer, was found guilty of manslaughter and 
#official misconduct.It's a breaking news in the community. So I use the tweets data to 
#see how many people are concerned about this matter. So I use a filter to filter the 
#tweets content by searching "Parade", and "Peter Liang". After getting these tweets data, 
#I used diff.py to calculate the arrival time differences between every tweet. When we get 
#the arrival time differences, we connect it with redis, a data structure server. So we 
#can know the average arrival time differences between every tweets in the real time. 
#If the average arrival time differences is very small, we can know that there are lots of 
#people are concerned about this matter. But if the average arrival time differences is 
#very large, we will assume there are only a few people are concerned about this issue.

#Please note this code doesn't contain user credentials to access Twitter API. Please
#apply user credentials by using your own Twitter account and fill it in before running
#this file.

#Import the necessary methods from tweepy library
#tweepy package is used for receive tweets in python
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#stdout is used for display the results in the terminal
from sys import stdout
#numpy is used for large, multi-dimensional arrays and matrices.
import numpy as np
#json import will help us deal with the output results. We will store the results in json
#format
import json
#import time will help us record the arrival time for every tweet
import time

#Variables that contains the user credentials to access Twitter API 
#Please note, in order to run this program successfully, you need to apply the user
#credentials by using your own twitter account.
access_token = "4877968799-gLwtwZwTlgCFvfyFQOIT1GE3r6uXacavNFclZV8"
access_token_secret = "SXWu5YYJBaOfun36uhL6kx34w0v6PICYD0kK1kTLwRFvt"
consumer_key = 	"CwlXnJW8gZth2Jqw2zoS0W3c4"
consumer_secret = "3BTHyWnRGbLQM0s4g2j8TM8IBAY4MYQBRgWSDwsfC1sAx45hOC"

#Set the rate to two.
rate = 2
#This is a listener prints the arrival time for every tweet contains Peter Liang, and 
#Parade
class StdOutListener(StreamListener):

    def on_data(self, data):
    	#print the arrival time in the json format
        print json.dumps({"t": time.time()})
        #force clean the cache, since WebSocket only update the output when refresh the cache.
    	stdout.flush()
    	#Set the sleep time. Generate a random exponential distribution of the sleep time
    	time.sleep(np.random.exponential(rate))
    	return True
	#Deal with the error, and print the error so that the error is easy to catch and debug.
    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: "Parade", and 
    #"Peter Liang"
    stream.filter(track=['Parade', 'Peter Liang']) 
    

    