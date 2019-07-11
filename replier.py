# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:12:37 2019

@author: Inki
"""
from threading import Thread
import tweepy
import time
import wikipedia
from textblob import TextBlob
import random 
import keys
import log

auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

class replier(Thread):
    
    FILE_NAME = 'last_seen_id.txt'
    
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
    
    def tag(self,text):
        try:
            tags={tag.strip("#") for tag in text.split() if tag.startswith("#")}
            tags=list(tags)
            return tags[0]
        except:
            pass
    
    
    def detectlenguage(self, tweet):
            b = TextBlob(tweet)
            if b.detect_language()=="en":
                return "en"
            else:
                return b.detect_language()
    
        
    def wikiurl(self, text,tweet):
        try:
                log.log("wikipedia.link(text)", flush=True)
                return wikipedia.page(self.detectlenguage(tweet)).url
    
        except:
                log.log("wikipedia.search(text)", flush=True)
                return "https://"+self.detectlenguage(tweet)+".wikipedia.org/wiki/" + text
        
    def othermentions(self, mention):
        try:
            ListaMencionesFiltrada=(list(filter(lambda name:
        name["screen_name"] != "WikiReply", api.get_status(mention.id)._json["entities"]["user_mentions"])))
            nombreslista=[]      
            for mencionados in ListaMencionesFiltrada:
                nicks=("".join(("@",mencionados['screen_name'])))
                nombreslista.append(nicks)
            
            return(str(' '.join(nombreslista)))
        except:
            return ("")
        
    def run(self):
        self.reply_to_tweets() 
    
    time.sleep(3)
    log.log("3secondswaited before reply to tweets")
        
    def reply_to_tweets(self):
        while True:
            log.log('retrieving and replying to tweets...')
            time.sleep(1)
            log.log("1 secondswaited after retrieving and replying to tweets.. ")
            
    
            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
            # NOTE: We need to use tweet_mode='extended' below to show
            # all full tweets (with full_text). Without it, long tweets
            # would be cut off.
            mentions = api.mentions_timeline(last_seen_id,
                                tweet_mode='extended')
           
            for mention in reversed(mentions):
                time.sleep(3)
                log.log("3 secondswaited in for mention in reversed(mentions)")
                log.log('checking...', flush=True)
                log.log(str(mention.id) + ' - ' + mention.full_text, flush=True)
               
                tweet=mention.full_text.lower()
                log.log('checkin1g...', flush=True)
                hashtag=self.tag(tweet)
                log.log('responding back...', flush=True)
                
                api.update_status('@' + mention.user.screen_name + " "
                            + self.wikiurl(hashtag,tweet)+ " " 
                            + self.othermentions(mention) ,
                            mention.id)
                
                last_seen_id = mention.id
                self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                log.log('respondido...', flush=True)
            time.sleep(5)
            log.log("5secondswaited at the end of for mention in reversed(mentions)")

if __name__== "__name__":
    responder=replier()
    responder.start()
