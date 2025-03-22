from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


ckey="CH7wf11TQ0hg0bM8nFN70Ro71"
csecret="RczXaf9RWitDBhEbnMBbAD33IPPBVfRqEzAzQnCKHEjyeJlY0I"
atoken="915577567851118592-lSeG9wV9bg8tWt2ImiIB1lQfpTFlK3r"
asecret="RP070Ew1WnHffHNyJjudyx22sqDhMiNR9MKxYfYqCbArn"
class listener(StreamListener):
	def on_data(self, data):
		all_data = json.loads(data)
		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()
		return True
	def on_error(self, status):
		print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Amit Shah"])

