import tweepy

from keys import *

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
num_tweets = 0
for mention in mentions:
    user_id = mention.text[15:]
    if "@" in user_id:
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
        ' tweets, not including retweets, user '+ user_id +' has amassed ' + str(fav_count) + ' likes and ' + str(ret_count) + ' retweets while having '+ str(follower_count) + ' followers')




