from tasks import get_unique_tweets

counts = [0,0,0,0,0,0,0]
words = ["han","hon","den","det","denna","denne","hen"]

tweetpointer = 0
tweetnum = 19

while(tweetpointer <= tweetnum):
    url = "http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_" + str(tweetpointer) + ".txt"
    (words,fcounts) = get_unique_tweets(url) 
    print(words,fcounts)
    for c in counts:
        c += fcounts[counts.index(c)]
    tweetpointer += 1;
print(words,counts)
data = {}
for word in words:
    data[word] = count[words.index(word)]
json_data = json.dumps(data)
return json_data
