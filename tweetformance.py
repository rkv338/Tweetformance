import tweepy
import time
from keys import *

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
repliedIds = []

def reply_tweets():
    mentions = api.mentions_timeline()
    num_tweets = 0
    for mention in mentions:
        tweetId = mention.id
        if tweetId not in repliedIds:
            user_id = mention.text[15:]
            if "-" in user_id:
                user_id = user_id[1:]
                follower_count = api.get_user(user_id).followers_count
                user_statuses = api.user_timeline(user_id)
                print(follower_count)
                fav_count = 0
                ret_count = 0
                if user_statuses:
                    for status in user_statuses:
                        if not hasattr(status, "retweeted_status"):
                            num_tweets += 1
                            fav_count += status.favorite_count
                            ret_count += status.retweet_count
                api.update_status('@' + mention.user.screen_name + ' in the past '+ str(num_tweets) + 
                ' tweets, not including retweets, user '+ user_id +' has amassed ' + str(fav_count) + ' likes and ' + str(ret_count) + ' retweets while having '+ str(follower_count) + ' followers', tweetId)
                repliedIds.append(tweetId)

while True:
    reply_tweets()
    time.sleep(15)


