# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:08:47 2019

@author: Inki
"""
from threading import Thread
import tweepy
import time
import wikipedia
import random 
import keys
import log

auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


class randomposting(Thread):
    log.log("inside class randompisting")
    def run(self):
        self.summary()
        
    def summary(self):
        while True:
            wikipedia.set_lang("es")
            log.log("buscando pagina random")
            try:
                randompage = wikipedia.random()
                summary = wikipedia.summary(randompage)
                link= wikipedia.page(randompage).url
                tweet= summary + link  
            
            except:
                continue 
                
            else: 
                if len(tweet)<= 280:
                    api.update_status(tweet)
                    log.log(tweet)
                    a=(random.randint(1, 3600))
                    log.log("dormir durante {0} segundos".format(a))
                    time.sleep(a)
                else:
                    a=(random.randint(1, 600))
                    log.log("dormir sin imprimir durante {0} segundos".format(a))
                    time.sleep(a)

#            finally:
#                logger.info("Time if error {time}".format(time))
                    
if __name__== "__name__":
                    
    postear=randomposting()
    postear.start()  