# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 01:22:51 2019

@author: Inki
"""
import tweepy
import time
import random 
import keys
import log


auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
api = tweepy.API(auth, wait_on_rate_limit=True)


def follow():
     import trends

     followers=trends.b().user.followers_count
     if followers > 1000 and followers < 1000000 :
     
         valor=(trends.b().user.followers_count)/random.randint(1,50)   
         print("Con {0} followers, Valor {1} para seguir a {2}".format
         (followers, valor, trends.b().user.screen_name ))
         if valor >= 2000:
             api.create_friendship(screen_name=trends.b().user.screen_name)
             print("Seguido a {0}".format(trends.b().user.screen_name))
             
             return