import tweepy

from keys import *

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
for mention in mentions:
    user_id = mention.text[15:]
    if "@" in user_id:
        print(user_id[1:])
#print(api.user_timeline('FSqueeze'))
# mentionsdict = mentions[0].__dict__.keys()
# print(mentions[0].text)



