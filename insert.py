#!/usr/local/bin/python

#credit to Columbia University Storytelling with Stream Data Course

#This file will help us put the arrival time differences between every tweet into redis. 
#Then we can calculate the average arrival time differences in the real time. 

#Please note, in order to run insert.py file successfully, you need to make sure redis is 
#connected. If you noticed you are disconnected with redis, please run the following 
#command in the terminal to connect to redis.

#$nohup redis-server &
#$ps aux | grep redis

#After running these two commands, you should see something like:

#redis    13319  0.0  0.0   2884  1056 ?        Ss   10:54   
#0:00 /usr/bin/redis-server /etc/redis/redis.conf

#which means you are now connected with redis. Now, let's run insert.py file.

#import the packages we need. 
#import json will help us load the arrival time for every tweet in json format.
#And it will also help us save the time differences in json format.
import json
#import stdout will let us see the output in the terminal
import sys
#import redis, a data structure server. Redis will give us support so that we can write
#and read data in the real time and at the same time.
import redis

#let's connect to radis
conn = redis.Redis()

#Read the time differences provided by diff.py file, and store the data via Redis
while 1:
	#Read the time differences provided by diff.py file
    line = sys.stdin.readline()
    d = json.loads(line)
    #record the time differences between every tweet
    delta = d["delta"]
    #record the arrival time for every tweet
    time = d["t"]
    #set the key to hold the arrival time and time differences for 120 seconds
    conn.setex(time, delta, 120)
    #print the arrival time and arrival time differences in the terminal
    print json.dumps({"time":time, "delta":delta})