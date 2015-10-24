import urllib2
import json
import itertools
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def count_pronouns():
    words = ["han","hon","den","det","denna","denne","hen"]
    data = {}
    for word in words:
        data[word] = 0
    tweetpointer = 0
    tweetnum = 0

    while(tweetpointer <= tweetnum):
        url = "http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_" + str(tweetpointer) + ".txt"
        (words,fcounts) = get_unique_tweets(url) 
        for c in fcounts:
            word = words[fcounts.index(c)]
            data[word] = str(int(data[word]) + c)
        tweetpointer += 1;
    json_data = json.dumps(data)
    return(json_data)

@app.task
def get_unique_tweets(url):

    counts = [0,0,0,0,0,0,0]
    words = ["han","hon","den","det","denna","denne","hen"]

    data = urllib2.urlopen(url)
    for line in data:
        while True:
            try:
                jfile = json.loads(line)
                if not(jfile['text'].startswith("RT")):
                    for word in words:
                        counts[words.index(word)] += jfile['text'].count(word)
                break
            except ValueError:
                try:
                    line+= next(data)
                except StopIteration:
                    return (words,counts)
                    
    return (words,counts)
