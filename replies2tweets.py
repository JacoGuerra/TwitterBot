# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 02:50:33 2019

@author: Inki
"""

replies=[] 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  
for full_tweets in tweepy.Cursor(api.user_timeline,screen_name=name,timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:'+name,result_type='recent',timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
      if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
        replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:
       print("Replies :",elements)
  replies.clear()
#The above code will fetch 10 recent tweets of
# an user(name) along with the replies to that ç
# particular tweet.The replies will be saved on to a list named replies. 
# You can retrieve more tweets by increasing the items count (eg:items(100)).
  
#  Here's a work around to fetch replies of a tweet made by "username" using the rest API using tweepy
#
#1) Find the tweet_id of the tweet for which the replies are required to be fetched
#
#2) Using the api's search method query the following (q="@username", since_id=tweet_id)
#    and retrieve all tweets since tweet_id
#
#3) the results matching the in_reply_to_status_id to tweet_id is the replies for the post.