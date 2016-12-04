from twitter import OAuth
from twitter import Twitter
import os

t = Twitter(auth=OAuth(os.getenv('ACCESS_TOKEN'),
                       os.getenv('ACCESS_TOKEN'),
                       os.getenv('CONSUMER_KEY'),
                       os.getenv('CONSUMER_SECRET')))

pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)

statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)
