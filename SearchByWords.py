# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:19:33 2019

@author: Inki
"""
import random
import tweepy
import keys
import log
from datetime import date
import sqlite3
import time
auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
api = tweepy.API(auth, wait_on_rate_limit=True)

auth1 = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth1.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api1 = tweepy.API(auth1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#auth = tweepy.OAuthHandler(keys.Consumer_Key_Trends, keys.CONSUMER_SECRET_Trends)
#auth.set_access_token(keys.ACCESS_KEY_Trends, keys.ACCESS_SECRET_Trends)
#api = tweepy.API(auth, wait_on_rate_limit=True)

def load_list():
    with open("200words.txt", 'r') as f:
        words_list = [line.strip() for line in f]
        return (words_list)

def search_tweets():
#    words_list=load_list()
#    word= random.choice(load_list())
    return api.search(q=random.choice(load_list()), lang="en",  tweet_mode='extended')

def filter_tweets():
    while True:
        print("durmiendo 5 seugnods____________________")
        time.sleep(5)

        for tweet in search_tweets():
    #        try:
    #         tweet=tweets.pop()
    #        except Exception as e:
    #             print(str(e))
    #             continue
            if 100 < tweet.user.followers_count and not 'media' in tweet.entities and (tweet.lang == "es" or tweet.lang == "en") \
                     and '@' not in tweet.full_text and ' http' not in tweet.full_text:
                         lista=[]
                         user_name=(tweet.user.screen_name)
                         followers_count=(tweet.user.followers_count)
                         user_id=(tweet.user.id)
                         full_text1=(tweet.full_text) #Para quitar las comillas de los tweets para que SQL no de problemas
                         full_text = full_text1.replace('"', '*')
                         try:
                             hashtags=tweet.entities["hashtags"][0]["text"]  #en caso de que el tweet tenga hashtags para evitar errores
                         except:
                             hashtags= "NoHashtag"
                         tweet_id=(tweet.id)
                         retweet_count=(tweet.retweet_count)
                         favorite_count=(tweet.favorite_count)
                         lang=(tweet.lang)
                         dates=(date.today().strftime("%m/%d/%y"))
                         lista.extend((full_text, retweet_count, favorite_count, followers_count, hashtags, user_name,  user_id, tweet_id, lang, dates))
                         print(lista)

#                         for full_tweets in tweepy.Cursor(api.user_timeline,screen_name=tweet.user.screen_name,timeout=10).items(10):
#                           for tweet in tweepy.Cursor(api1.search,q='to:'+tweet.user.screen_name,result_type='recent',timeout=10, tweet_mode='extended').items(1000):
#                            if hasattr(tweet, 'in_reply_to_status_id_str'):
#                               for tweet in  tweepy.Cursor(api.search,q='to:'+tweet.user.screen_name,result_type='recent',timeout=10, tweet_mode='extended').items(1000):
#                                  if tweet.in_reply_to_status_id_str==full_tweets.id_str and tweet.favorite_count > 2 and not 'media' in tweet.entities\
#                                  and (tweet.lang == "es" or tweet.lang == "en") and ' http' not in tweet.full_text:
#                                     reuser_name=(tweet.user.screen_name)
#                                     refollowers_count=(tweet.user.followers_count)
#                                     reuser_id=(tweet.user.id)
#                                     refull_text=(tweet.full_text)
#                                     try:
#                                         hashtags=tweet.entities["hashtags"][0]["text"]
#                                     except:
#                                         hashtags= "NoHashtag"
#                                     rehashtags = hashtags
#                                     retweet_id=(tweet.id)
#                                     reretweet_count=(tweet.retweet_count)
#                                     refavorite_count=(tweet.favorite_count)
#                                     relang=(tweet.lang)
#                                     redates=(date.today().strftime("%m/%d/%y"))
#                                     print("__________")
#                                     print(full_text)
#                                     print(refull_text)
#                                     print("__________")
#                                     lista.extend((refull_text, reretweet_count, refavorite_count, refollowers_count, rehashtags, reuser_name,  reuser_id, retweet_id, relang, redates))
#                                  else:
#                                     continue



#def replies_2_tweets():


filter_tweets()