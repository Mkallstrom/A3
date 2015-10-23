#from tasks import counter
import urllib2
import json
import itertools

han = 0
hon = 0
den = 0
det = 0
denna = 0
denne = 0
hen = 0

def get_unique_tweets(data):
    objs = []
    for line in data:
        if len(objs) > 100:
            break
        while True:
            try:
                jfile = json.loads(line)
                if not(jfile['text'].startswith("RT")):
                    objs.append(jfile)
                break
            except ValueError:
                line+= next(data)

    return objs

def count_words(objs):
    for obj in objs:
        global han
        global hon
        global den
        global det
        global denne
        global denna
        global hen
        han += obj['text'].count("han")
        hon += obj['text'].count("hon")
        den += obj['text'].count("den")
        det += obj['text'].count("det")
        denna += obj['text'].count("denna")
        denne += obj['text'].count("denne")
        hen += obj['text'].count("hen")

tweetnum = 19
tweetpointer = 0

while(tweetpointer <= tweetnum):
    global tweetpointer
    data = urllib2.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_" + str(tweetpointer) + ".txt")
    objs = get_unique_tweets(data)
    count_words(objs)
    print("Han: " + str(han))
    tweetpointer += 1;
#counter()
