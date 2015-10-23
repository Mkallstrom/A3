import urllib2
import json
import itertools
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def get_unique_tweets(url):

    counts = [0,0,0,0,0,0,0]
    words = ["han","hon","den","det","denna","denne","hen"]

    print("Now opening " + url)
    data = urllib2.urlopen(url)
    print("Url successfully opened.")
    for line in data:
        while True:
            try:
                jfile = json.loads(line)
                if not(jfile['text'].startswith("RT")):
                    for word in words:
                        counts[words.index(word)] += count_word(jfile, word) 
                break
            except ValueError:
                try:
                    line+= next(data)
                except StopIteration:
                    return (words,counts)
                    
    return (words,counts)

@app.task
def count_word(obj, word):
    count = obj['text'].count(word)
    return count
