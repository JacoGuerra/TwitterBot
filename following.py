# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 01:24:52 2019

@author: Inki
"""

from threading import Thread
import tweepy
import time
import random 
import keys
import log


auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
api = tweepy.API(auth, wait_on_rate_limit=True)



class following(Thread):
    FILE_NAME = 'RTlast_seen_id.txt'
    log.log("dentro de following")
    
    def run(self):
        self.follow()
    
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
    
#    def store_followrs() 
#        with open('following.txt') as csv_file:
#            csv_reader = csv.reader(csv_file, delimiter=',')
#            line_count = 0
#            for row in csv_reader:
#                if line_count == 0:
#                    print(f'Column names are {", ".join(row)}')
#                    line_count += 1
#                else:
#                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                    line_count += 1
#            print(f'Processed {line_count} lines.')

    def follow(self):
        while True:
            log.log("dentro de  def follow(self):") 
            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
#            lasttweets=api.home_timeline(since_id=last_seen_id, tweet_mode='extended', count=1)
            lasttweets=api.home_timeline(tweet_mode='extended', count=3)
            log.log(lasttweets)
            for tweet in reversed(lasttweets) :
                lista=api.user_timeline(screen_name=tweet.user.screen_name, count=10)
                log.log(lista)
                count=0
                valoraciontotal=0
                for lista in lista:
                    log.log(lista.text)
                    followers=lista.user.followers_count
                    valor=(followers)/random.randint(1,500)
                    log.log("Con {0} followers, Valor {1} para seguir a {2}".format(followers, valor, lista.user.screen_name))
                    count += 1
                    valoraciontotal+=valor
                    
                    if valor >= 2000:
                                api.create_friendship(screen_name=lista.user.screen_name)
                                log.log("Seguido a {0}".format(lista.user.screen_name))
#                                time.sleep(random.randint(5, 120))
                                last_seen_id = tweet.id
                                self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                    else:
                        log.log("No seguido a {0}".format(lista.user.screen_name))
                media=valoraciontotal/count
                log.log("Media de valores {0} para {1} muestras".format(media, count))
                last_seen_id = tweet.id
                self.store_last_seen_id(last_seen_id, self.FILE_NAME)
                
                        
#
#    def follow(self):
#        while True:
#            last_seen_id = self.retrieve_last_seen_id(self.FILE_NAME)
#            lasttweets=api.home_timeline(since_id=last_seen_id, tweet_mode='extended', count=1)
#            for tweet in reversed(lasttweets) :
#        
                         