import urllib2
import json
import itertools
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def get_unique_tweets(data):
    print("Now getting unique tweets")
    objs = []
    for line in data:
        while True:
            try:
                jfile = json.loads(line)
                if not(jfile['text'].startswith("RT")):
                    objs.append(jfile)
                break
            except ValueError:
                try:
                    line+= next(data)
                except StopIteration:
                    print("Returned from exception")
                    return objs
                    
    print("Returned normally")
    return objs

@app.task
def count_word(objs, word):
    print("Now counting occurences of " + word)
    count = 0
    for obj in objs:
        count += obj['text'].count(word)
    print("Found " + str(count) + " occurences of " + word)
    return count

@app.task
def run():
    counts = [0,0,0,0,0,0,0]
    words = ["han","hon","den","det","denna","denne","hen"]

    tweetpointer = 0
    tweetnum = 19
    while(tweetpointer <= tweetnum):
        data = urllib2.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_" + str(tweetpointer) + ".txt")
        objs = get_unique_tweets(data)
        for word in words:
            counts[words.index(word)] += count_word(objs, word)
        tweetpointer += 1;
    return (words, counts)
