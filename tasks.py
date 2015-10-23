import urllib2
import json
import itertools
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def get_unique_tweets(url):
    print("Now opening " + url)
    data = urllib2.urlopen(url)
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
