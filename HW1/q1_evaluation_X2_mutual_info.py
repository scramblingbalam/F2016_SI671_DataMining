with open("../tweets.txt","r")as tweetfile:
	tweets = tweetfile.read()
	print type()tweets