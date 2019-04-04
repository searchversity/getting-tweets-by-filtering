from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

ckey = 'LCh9rQWxpAyBnN6MXGi9OIcZw'
csecret = 'UgyichsAKEbWecErJYomKjl4w24LUdPDBp1XgXnWP5JZTXEQPW'
atoken = '1112919238673494016-6FAJEaT5lrwStnkw9fyQme3Fq7Y4q7'
asecret = 'eEZeAuXBB1tpRtqTB191ftQgjHEtqZ35v9q2o7CK6RCLK'

class listener (StreamListener):

    def on_data (self, data):
        print (data)
        return True

    def on_error (self, status):
        print (status)

auth = OAuthHandler (ckey, csecret)
auth.set_access_token (atoken, asecret)
twitterStream = Stream (auth, listener())
twitterStream.filter(track = ["car"])
