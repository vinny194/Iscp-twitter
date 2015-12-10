from TwitterAPI import TwitterAPI
import json
import time
import Tkinter

saveFile = "data.sav"

api = TwitterAPI("iVv0T3zCh270ZRJLDCkqxf71w", "QnGe3MVFG5T0BX5fqsA5GjjpWqpy30OVNBJPxBbw4Zyee1dorQ", "4274488889-WNLq6z2aYNWEN1chbfra5AwfLxrXwtvzYHPeF27", "mcqLmwWvwkJ3rqAXe0hnH1mHYxAVmTL4wT6JEtb6Vbelp")
tweets = []

def load():
	global tweets
	tweets = json.load(open(saveFile))	

def save():
	json.dump(tweets, open(saveFile,'w'))
	
def getTweets():
	r = api.request('statuses/filter', {'track':'cat'})
	
	print("aantal tweets "+str(len(tweets)))
	
	for item in r:
		try:
			tweets.append(item);
			print("aantal tweets "+str(len(tweets)))
		except Exception as inst:
			print(inst)
	
	print("aantal tweets na: "+str(len(tweets)))

def printTweets():
	print(json.dumps(tweets))
	
def clear():
	tweets = []

def get1000Tweets():
	while len(tweets) < 1000 :
		getTweets()
		time.sleep(1)

def removeDupe():
	global tweets
	tweets = json.dumps(tweets)
	tweets = { each['id'] : each for each in tweets }.values()
