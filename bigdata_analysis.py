# -*- coding: utf-8 -*-

#This code implements the first two methods - a word frequency and hashtag frequency counter
import json
import string
import re

tweets_data_path = '../Project/Data/tweetStream200kSample'

hashtagList = {}
wordList = {}
counter = 0
tweets_file = open(tweets_data_path+'.txt', "r")

#This file includes stop words, Twitter-related words, and inappropriate words
scratchText = open('scratchWords.txt').read()	

for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
    #Code to store counts for all hashtags
	for hashtag in tweet['entities']['hashtags']:
		tag = hashtag['text']
		if tag not in scratchText:
			if tag in hashtagList:
				hashtagList[tag] += 1
			else:
				hashtagList[tag] = 1
	#Code to store counts for all words
	text = tweet['text'].split()
	for word in text:
		#Parsing words to strip all punctuation and convert to lower case
		parsed = ''.join(c for c in word if c not in string.punctuation)
		parsed = parsed.lower()
		if parsed not in scratchText:
			if parsed in wordList:
				wordList[parsed] += 1
			else:
				wordList[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'There are', counter/2, 'tweets'

#Storage into data
words = open(tweets_data_path+'Words.txt',"w")
json.dump(sorted(wordList.items(), key=lambda x:x[1], reverse=True), words)
words.close()
print 'There are', len(wordList), 'words'

hashtags = open(tweets_data_path+'Hashtags.txt',"w")
json.dump(sorted(hashtagList.items(), key=lambda x:x[1], reverse=True), hashtags)
hashtags.close()
print 'There are', len(hashtagList), 'hashtags'