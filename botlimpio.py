# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:11:16 2019

@author: Inki
"""
from threading import Thread
import tweepy
import time
import wikipedia
from textblob import TextBlob
import random 
import keys

# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.

# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/


#ends_with(suffix, start=0, end=9223372036854775807)
#Returns True if the blob ends with the given suffix.
#
#endswith(suffix, start=0, end=9223372036854775807)
#Returns True if the blob ends with the given suffix.
print('this is my twitter bot')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


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
                print("wikipedia.link(text)", flush=True)
                return wikipedia.page(self.detectlenguage(tweet)).url
    
        except:
                print("wikipedia.search(text)", flush=True)
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
    print("3secondswaited before reply to tweets")
        
    def reply_to_tweets(self):
        while True:
            print('retrieving and replying to tweets...', flush=True)
            time.sleep(1)
            print("1 secondswaited after retrieving and replying to tweets.. ")
            
    
            # DEV NOTE: use 1060651988453654528 for testing.
            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
            # NOTE: We need to use tweet_mode='extended' below to show
            # all full tweets (with full_text). Without it, long tweets
            # would be cut off.
            mentions = api.mentions_timeline(
                                last_seen_id,
                                tweet_mode='extended')
           
            for mention in reversed(mentions):
                time.sleep(3)
                print("3 secondswaited in for mention in reversed(mentions)")
                print('checking...', flush=True)
                print(str(mention.id) + ' - ' + mention.full_text, flush=True)
               
                tweet=mention.full_text.lower()
                print('checkin1g...', flush=True)
                hashtag=self.tag(tweet)
                print('responding back...', flush=True)
                
                api.update_status('@' + mention.user.screen_name + " "
                            + self.wikiurl(hashtag,tweet)+ " " + self.othermentions(mention) ,
                            mention.id)
                
                last_seen_id = mention.id
                self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                print('respondido...', flush=True)
            time.sleep(5)
            print("5secondswaited at the end of for mention in reversed(mentions)")


class randomposting(Thread):
    print("inside class randompisting")
    print("dormir 15 segundos a ramdom posting")
    def run(self):
        self.summary()
        
    def summary(self):
        while True:
            wikipedia.set_lang("es")
            print("buscando pagina random")
            randompage = wikipedia.random()
            summary = wikipedia.summary(randompage)
            link= wikipedia.page(randompage).url
            tweet= summary + link           
            if len(tweet)<= 280:
                api.update_status(tweet)
                print(tweet)
                a=time.sleep(random.randint(1, 3600))     
                print(a)
            else:
                print("no se puede imprimir!! demaisado largp")

class retweets(Thread):
    FILE_NAME = 'RTlast_seen_id.txt'
    
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
        while True:
            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
            lasttweets=api.home_timeline(last_seen_id, tweet_mode='extended')
            
            for tweet in reversed(lasttweets) :
                print("dentro de for tweet in reversed(lasttweets) : 3s") 
                time.sleep(3)
                print(' ')
                text=tweet.full_text
                b = TextBlob(text)
                if b.detect_language()=="es":
                    print("nuevo tweet en español")
                    print(tweet.user.screen_name)
                    print(tweet.user.followers_count)
                    retweet=(tweet.retweet_count)
                    favorite=(tweet.favorite_count)
                    valor=random.randint(1,1000)+(retweet)/10+favorite/10
                    print("Num.RT {0},Num.Favs{1}, total={2}".format(retweet, favorite, valor))
                    print(" ")
                    if valor>= 900:
                        api.retweet(tweet.id)
                        print(tweet.full_text)
                        print(" ")
                
                    last_seen_id = tweet.id
                    self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                    print('revisado...')
                    print(' ')
#         




##    t1 = Thread(target=replier.self.reply_to_tweets)
#    multiplicar=multipling()
#responder=replier()
#responder.start()

#
postear=randomposting()
postear.start()  

retweets=retweets()
retweets.start()