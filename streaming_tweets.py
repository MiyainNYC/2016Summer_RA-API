from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sqlite3
import time
import json


conn = sqlite3.connect("tweets.db")

cur = conn.cursor()
#cur.execute("create table tweets (created_at, tweet, location, retweet_count)")


#consumer key, consumer secret, access token, access secret.
ckey="JVeuqL04E63tWRktUjuEmjW9H"
csecret="KJ9hnGzX9skuLedC7BGw8hDwhgaCpeLwur1stP6RLT17I8nmjs"
atoken="3480144377-AATiPTS9QKj3vfRvVg8IPBwCbdgltJLXizqOFtC"
asecret="EeAx9cBwDnEbiuesKeOzKSZKFj3VqJoNLzo3Rg9wg3gEQ"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        
        tweet = all_data["text"]
        created_at = all_data['created_at']
        location = all_data["user"]["location"]
        retweet_count = all_data['retweet_count']
        
        cur.execute('''INSERT INTO tweets (created_at, tweet, location, retweet_count) values (?,?,?,?)''',(created_at, tweet, location, retweet_count))

        conn.commit()

        print((created_at))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["delta"])