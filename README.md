In this homework, I chose to use tweets as a stream data. However, this time, I tried to 
find a specific content in tweets, which is the key words about the “Support Peter Liang”.

Recently, a breaking news aroused the concern of the community. According to Wikipedia, 
Peter Liang, a New York Police Department officer, was found guilty of manslaughter and 
official misconduct. 

The victim, Akai Gurley, is a 28-year-old African-American man. Liang and another police 
officers entered a pitch-dark, unlit stair well, Liang shot the victim. Gregory and his 
girlfriend entered the seventh floor stairwell, 14 steps below them. The bullet 
ricocheted off a wall, then hit in the chest of Gurley. He later died in hospital.

People started to talking about if the criminal charges are justice. New York City Police 
Commissioner Bill Bratton declared the shooting to be an accident and that Gurley was 
a "total innocent". On February 20, 2016, according to wikipedia, there were 15000 people
protested on behalf of Liang in New York, and thousands other protested in 42 other cities
across the United States at the same time.

It's a breaking news in the community. So I use the tweets data to see how many people
are concerned about this matter. So I use a filter to filter the tweets content by 
searching "Parade", and "Peter Liang". After getting these tweets data, I used diff.py
to calculate the arrival time differences between every tweet. When we get the arrival time 
differences, we connect it with redis, a data structure server. So we can know the average
arrival time differences between every tweets in the real time. If the average arrival time
differences is very small, we can know that there are lots of people are concerned about 
this matter. But if the average arrival time differences is very large, we will assume
there are only a few people are concerned about this issue.

I run this code on February 19 and 20, which is the time the parade was calling on people.
So the average arrival time differences became very small, it's less than one. On February
22, I run the code again. This time, because the parade was passed by two days, but people
still remember the Peter Liang issue, the average arrival time differences is about 3.5.
I will assume maybe after a month, the average arrival time differences will drop down to
4 or 5. So I set my alert threshold as the following:

If the average arrival time differences is less than 1.5, I will call this matter a 
"hot issue" for the community. If the average arrival time differences is between 1.5 and
3.7, I will call this matter a "still concerned issue". If the average arrival time 
differences is larger than 3.7, I will call it "normal issue".

In order to successfully get the correct results, please follow the following steps.

First, run the twitter_streaming.py file. Please use your own Twitter account to apply 
the user credentials to access Twitter API. Then, this file will get the tweets data with
content contains "Peter Liang", and "Parade". Also, this file will record the arrival time
for every tweet, which will be further used in the calculation of the arrival time 
differences. Please note the arrival time will be saved in json format.

Second, run the diff.py file. In this file, we will calculate the arrival time differences
between every tweet. You can see the arrival time differences in the terminal.  

Then, let's run insert.py file. This file will help us put the arrival time differences 
between every tweet into redis. Then we can calculate the average arrival time differences
in the real time. Please note, in order to run insert.py file successfully, you need to 
make sure redis is connected. If you noticed you are disconnected with redis, please run 
the following command in the terminal to connect to redis.

$nohup redis-server &
$ps aux | grep redis

After running these two commands, you should see something like:

redis    13319  0.0  0.0   2884  1056 ?        Ss   10:54   
0:00 /usr/bin/redis-server /etc/redis/redis.conf

which means you are now connected with redis. Now, let's run insert.py file.

Next, let's run ave.py file. This file will calculate the average arrival time differences
in the real time. We will use this result as a way to identify if this issue is a hot issue.

Finally, let's open the webpage.html file to see the analytics results on the webpage.
