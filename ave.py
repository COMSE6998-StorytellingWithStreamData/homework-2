#!/usr/local/bin/python

#credit to Columbia University Storytelling with Stream Data Course

#import the package we need
#import redis, a data structure server. Redis will give us support so that we can write
#and read data in the real time and at the same time.
import redis
#import json will help us load the arrival time for every tweet in json format.
#And it will also help us save the time differences in json format.
import json
#import time will help us record the arrival time for every tweet
import time
#import stdout will let us see the output in the terminal
import sys

#connect to redis, so that we can calculate the average arrival time differences in the
#real time and at the same time when the data is written into redis
conn = redis.Redis()

#start calculating the average arrival time differences and analyzing if this issue is
#a hot issue
while 1:
	#credit to https://pypi.python.org/pypi/redis
	#Pipelines are a subclass of the base Redis class that provide support for buffering 
	#multiple commands to the server in a single request. They can be used to dramatically 
	#increase the performance of groups of commands by reducing the number of back-and-forth 
	#TCP packets between the client and server.
    pipe = conn.pipeline()

	#get the key, which will lead us to find the arrival time and the arrival time 
	#differences stored by insert.py file
    keys = conn.keys()

	#get the arrival time and arrival time differences
    values = conn.mget(keys)

    try:
    	#deltas will store all the arrival time differences between every two tweets
        deltas = [float(v) for v in values]
        #Catch the error, so that we can know which key has the error. It will help us 
        #debug the error
    except TypeError:
    	#if there is an error, print the keys
        print keys
        continue

	#for every element in delta, which means for all the arrival time differences we get
	#we calculate the average arrival time differences
    if len(deltas):
    	#The average arrival time differences equals to the sum of all the time differences
    	#divided by the number of time differences we get
        rate = sum(deltas)/float(len(deltas))
    #if we don't receive any time differences data, the rate value is zero
    else:
        rate = 0

    #Now let's start to analyze if this issue is a hot issue
    
#I run this code on February 19 and 20, which is the time the parade was calling on people.
#So the average arrival time differences became very small, it's less than one. On February
#22, I run the code again. This time, because the parade was passed by two days, but people
#still remember the Peter Liang issue, the average arrival time differences is about 3.5.
#I will assume maybe after a month, the average arrival time differences will drop down to
#4 or 5. So I set my alert threshold as the following:

#If the average arrival time differences is less than 1.5, I will call this matter a 
#"hot issue" for the community. If the average arrival time differences is between 1.5 and
#3.7, I will call this matter a "still concerned issue". If the average arrival time 
#differences is larger than 3.7, I will call it "normal issue".

#Now let's use code to accomplish what I said above.

#If the average arrival time differences is less than 1.5, I will call this matter a 
#"hot issue" for the community.
    if rate <= 1.5:
    	print 'hot issue'
    	#force clean the cache, since WebSocket only update the output when refresh the cache.
    	sys.stdout.flush()
    	
#If the average arrival time differences is between 1.5 and 3.7, I will call this matter 
#a "still concerned issue".
    elif 1.5 < rate < 3.7:
    	print 'still concerned issue'
    	#force clean the cache, since WebSocket only update the output when refresh the cache.
    	sys.stdout.flush()
    	
#If the average arrival time differences is larger than 3.7, I will call it "normal issue".
    else :
    	print 'normal issue'
    	#force clean the cache, since WebSocket only update the output when refresh the cache.
    	sys.stdout.flush()

	#set the sleep time equals to 0.5 second
    time.sleep(0.5)