# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:15:21 2019

@author: Inki
"""
from threading import Thread
import tweepy
import time
from textblob import TextBlob
import random 
import keys
import log



auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class retweets(Thread):
    FILE_NAME = 'RTlast_seen_id.txt'
    log.log("dentro de retweets")
    
    def run(self):
        self.retweettimeline()
    
    def retrieve_last_seen_id(self, file_name):
        f_read = open(file_name, 'r')
        last_seen_id = int(f_read.read().strip())
        f_read.close()
        return last_seen_id
    
    def store_last_seen_id(self, last_seen_id, file_name):
        f_write = open(file_name, 'w')
        f_write.write(str(last_seen_id))
        f_write.close()
        return
    
    def retweettimeline(self):
        log.log("dentro de retweettimeline")
        while True:
            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
            lasttweets=api.home_timeline(since_id=last_seen_id, tweet_mode='extended')
            
            for tweet in reversed(lasttweets) :
                log.log("dentro de for tweet in reversed(lasttweets) : 3s") 
                time.sleep(3)
                log.log(' ')
                text=tweet.full_text
                b = TextBlob(text)
                if b.detect_language()=="es" or b.detect_language()=="en":
                    log.log("nuevo tweet Name: {0} NumFollowers: {1} ID: {2}".format
                            (tweet.user.screen_name, tweet.user.followers_count, tweet.id ))
                    retweet=(tweet.retweet_count)
                    favorite=(tweet.favorite_count)
                    valor=random.randint(1,10000)+ (retweet)/random.randint(1,20)+ favorite/random.randint(20,100)
                    log.log("Num.RT {0},Num.Favs{1}, total={2}".format(retweet, favorite, valor))
                    log.log(" ")
                    if valor>= 9500:
                        api.retweet(tweet.id)
                        log.log(tweet.full_text)
                        log.log(" ")
                        a=(random.randint(10, 1000))
                        log.log("Dormir durante {0} segundos".format(a))
                        time.sleep(a)
                        
                
                    last_seen_id = tweet.id
                    self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                    log.log('revisado...')

                    log.log(' ')
                    
if __name__== "__name__":                    
    retweets=retweets()
    retweets.start()


#         