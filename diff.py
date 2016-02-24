#!/usr/local/bin/python

#credit to Columbia University Storytelling with Stream Data Course

#In this file, we will calculate the arrival time differences between every tweet. 
#You can see the arrival time differences in the terminal. 

#import the packages we need. 
#import json will help us load the arrival time for every tweet in json format.
#And it will also help us save the time differences in json format.
import json
#import stdout will let us see the output in the terminal
import sys

#First initial the time. Set the arrival time for the last tweet equals to zero.
last = 0
#Start read the arrival time for tweets given by twitter_streaming.py file.
#And calculate the arrival time differences.
while 1:
	#Read the arrival time for tweets given given by twitter_streaming.py file
    line = sys.stdin.readline()
    d = json.loads(line)
    #if this is the first arrival time, update the last arrival time equals to this 
    #arrival time
    if last == 0 :
        last = d["t"]
        continue
    #otherwise, the time differences equals to the differences between arrival time
    #and last arrival time 
    delta = d["t"] - last
    #print the arrival time differences in the terminal
    print json.dumps({"delta":delta, "t":d["t"]})
    #force clean the cache, since WebSocket only update the output when refresh the cache.
    sys.stdout.flush()
    #update the last time equals to this tweet's arrival time
    #prepare to calculate the next arrival time difference
    last = d["t"]
