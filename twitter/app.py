#pip install -U textblob
#python -m textblob.download_corpora

from TwitterAPI import TwitterAPI
import json
import afinn
import time
import tkinter as Tkinter
from map import Map
import nltk
from textblob import TextBlob

saveFile = "data.sav"

api = TwitterAPI("iVv0T3zCh270ZRJLDCkqxf71w", "QnGe3MVFG5T0BX5fqsA5GjjpWqpy30OVNBJPxBbw4Zyee1dorQ", "4274488889-WNLq6z2aYNWEN1chbfra5AwfLxrXwtvzYHPeF27", "mcqLmwWvwkJ3rqAXe0hnH1mHYxAVmTL4wT6JEtb6Vbelp")
tweets = []

def load():
	global tweets
	tweets = json.load(open(saveFile))	

def save():
	json.dump(tweets, open(saveFile,'w'))
	
def getTweets():
	r = api.request('statuses/filter', {'track':'cat','lang':'en'})
	
	print("aantal tweets "+str(len(tweets)))
	
	for item in r:
		try:
			if item['lang'] == 'en':
				tweets.append(item);
				print("aantal tweets "+str(len(tweets)))
		except Exception as inst:
			print(inst)
	
	print("aantal tweets na: "+str(len(tweets)))

def printTweets():
	print(json.dumps(tweets))
	
def clear():
	tweets = []

def showTweet(i):
	print (str(tweets[i]['sentiment'])+ " | "+ tweets[i]['text'])

def get1000Tweets():
	while len(tweets) < 1000 :
		getTweets()
		time.sleep(1)

def removeDupe():
	global tweets
	tweets = json.dumps(tweets)
	tweets = { each['id'] : each for each in tweets }.values()

def BTN_Load_Callback():
	load()
	print("aantal tweets "+str(len(tweets)))

def createWindow():
	top = Tkinter.Tk()
	
	BTN_Load = Tkinter.Button(top,text = "Load", command=BTN_Load_Callback)
	BTN_Load.pack();
	
	BTN_Map = Tkinter.Button(top,text = "map", command=createMap)
	BTN_Map.pack();
	
	BTN_NltkDownload = Tkinter.Button(top,text = "download NLTK", command=nltk.download)
	BTN_NltkDownload.pack();
	
	top.mainloop()

def createMap():
	map = Map(tweets)
	map.show()

def analyze():
	for tweet in tweets:
		try:
			sentiment = 0
			text = tweet['text']
			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment += sentence.sentiment.polarity
			print (sentiment)
			tweet['sentiment'] = sentiment
		except Exception as e:
			print (e)
	
createWindow()