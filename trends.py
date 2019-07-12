# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:38:07 2019

@author: Inki
"""
import time
from threading import Thread
import tweepy
import keys
import log
import json
#from textblob import TextBlob

auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
api = tweepy.API(auth, wait_on_rate_limit=True)

#data= json.loads(api.trends_available())
def lookingforplaces():
    for i in api.trends_available():
        name=i["name"]
        woeid=i["woeid"]
        suma=name, woeid
        log.log(suma)
        
def trends_place():
    
    places={
        "United States": 23424977,
        'Spain': 23424950
        }
    for value in places.values():
         for a in api.trends_place(value):
             for i in a["trends"]:
#                 b=i["name"]
#                 lng = TextBlob(b)
#                 time.sleep(0.2)
#                 if lng.detect_language()=="es" or lng.detect_language()=="en":
                 a=(i["name"])
                 a=api.search(a)
                 b=a.pop
                 print(b().text)
def searchs():                 
    a=api.search(trends_place())
    b=a.pop
    print(b()._json.id)
    
trends_place()  
#log.log(a)
#lookingforplaces()
## 
#searchs()