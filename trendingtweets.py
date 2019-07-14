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
import random 
import follow
import pickle 
import codecs


auth = tweepy.OAuthHandler(keys.Consumer_Key_Trends, keys.CONSUMER_SECRET_Trends)
auth.set_access_token(keys.ACCESS_KEY_Trends, keys.ACCESS_SECRET_Trends)
api = tweepy.API(auth, wait_on_rate_limit=True)

#data= json.loads(api.trends_available())
def lookingforplaces():
    for i in api.trends_available():
        name=i["name"]
        woeid=i["woeid"]
        suma=name, woeid
        log.log(suma)

        
        
def trendingtweets():
    
    places={
        "United States": 23424977,
        'Spain': 23424950
        }
    lista={}
    for value in places.values():
         for a in api.trends_place(value):
             for i in a["trends"]:
                 a=i["name"]
                 a=api.search(a)
                 try:
                     b=a.pop
                     lista.append(b())
                 except:
                    continue
                
#    with codecs.open("trendsinfo.txt", 'w', encoding='utf8') as f:
#          f.write(str(lista)) REVISAR SI DEVUELVE UNA LISTA VACIA O NO WTFFFFF
          
    with open('trendsinfo.pkl', "wb") as f:
         pickle.dump((lista), f)
                 
                 
                 
                 
def following():
     with open('trendsinfo.pkl', "rb") as f:
         b = pickle.load(f)

         print(b)
#         followers=b.followers_count
#         if followers > 1000 and followers < 1000000 :
#         
#             valor=(b.followers_count)/random.randint(1,50)   
#             print("Con {0} followers, Valor {1} para seguir a {2}".format
#             (followers, valor, b.screen_name ))
#             if valor >= 2000:
#                 api.create_friendship(screen_name=b.screen_name)
#                 print("Seguido a {0}".format(b.screen_name))              
#                         
#                 """De aqui voy a desviar al resto de modulos!
#                 los ejecuto con following(b) por ejempllo
#                 
#                 Tengo que aprender tambien a descartar resultados!
#                 """
                 
                     
                     



following()  
#log.log(a)
#lookingforplaces()
## 
#searchs()