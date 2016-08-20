from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sqlite3
import time
import json


conn = sqlite3.connect("tweets.db")

cur = conn.cursor()
cur.execute("create table tweets (screen_name,created_at, text, location, retweet_count, in_reply_to_screen_name,followers_count,language)")


#consumer key, consumer secret, access token, access secret.
ckey="JVeuqL04E63tWRktUjuEmjW9H"
csecret="KJ9hnGzX9skuLedC7BGw8hDwhgaCpeLwur1stP6RLT17I8nmjs"
atoken="3480144377-AATiPTS9QKj3vfRvVg8IPBwCbdgltJLXizqOFtC"
asecret="EeAx9cBwDnEbiuesKeOzKSZKFj3VqJoNLzo3Rg9wg3gEQ"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        text = all_data["text"]
        created_at = all_data['created_at']
        location = all_data["user"]["location"]
        retweet_count = all_data['retweet_count']
        screen_name = all_data["user"]["name"]
        language = all_data['user']["lang"]
        followers_count = all_data['user']["followers_count"]
        in_reply_to_screen_name = all_data["in_reply_to_screen_name"]
            
        cur.execute('''INSERT INTO tweets (screen_name,created_at, text, location, retweet_count, in_reply_to_screen_name,followers_count,language) values (?,?,?,?,?,?,?,?)''',(screen_name,created_at, text, location, retweet_count, in_reply_to_screen_name,followers_count,language))
        conn.commit()

        print((created_at))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["amazon cloud"])