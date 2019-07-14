# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:38:07 2019

@author: Inki
"""
from threading import Thread
import tweepy
import keys
import log
import json
#from textblob import TextBlob
import random 
from datetime import date
import databasetweets


auth = tweepy.OAuthHandler(keys.Consumer_Key_Trends, keys.CONSUMER_SECRET_Trends)
auth.set_access_token(keys.ACCESS_KEY_Trends, keys.ACCESS_SECRET_Trends)
api = tweepy.API(auth, wait_on_rate_limit=True)

#auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
#auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
#api = tweepy.API(auth, wait_on_rate_limit=True)


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
        'Spain': 23424950,
        "Madrid": 766273,
        "Zaragoza": 779063,
        "Valencia" :776688,
        "Baltimore" :2358820,
        "Las Vegas": 2436704,
        'Los Angeles':2442047
    }
    
    count=0
    for value in places.values():
         for a in api.trends_place(value):
#             print(a)
             print("__________________________________________________________________________")
             for i in a["trends"]:
#                 print(i)
                 a=i["name"]
                 tweet=api.search(a, tweet_mode='extended')
                 try:
                     tweet=tweet.pop()
                 except Exception as e:
                         print(str(e))
                         
                     
        #                 info=(json.dumps(a[0]._json, ensure_ascii=False).encode('utf8'))
#                 info=(json.dumps(a[0]._json))
                 if 100 < tweet.user.followers_count :
#                 and not 'media' in tweet.entities\
#                 and (tweet.lang == "es" or tweet.lang == "en") \
#                 and '@' not in tweet.full_text and ' http' not in tweet.full_text:
                     lista=[]
                     lista.append(tweet.user.screen_name)
                     lista.append(tweet.user.followers_count)
                     lista.append(tweet.user.id)
                     lista.append(tweet.full_text)
                     try:
                         hashtags=tweet.entities["hashtags"][0]["text"]
                     except:
                         hashtags= "NoHashtag"
                     lista.append(hashtags)
                     lista.append(tweet.id)
                     lista.append(tweet.retweet_count)
                     lista.append(tweet.favorite_count)
                     lista.append(tweet.lang)
                     lista.append(date.today().strftime("%m/%d/%y"))
                     
                     print(lista)
                    
#                     print(tweet.entities["hashtags"])
#                 except:
#                     continue
##                 print(tweet)
                 
#                 lista.append(info)
#                 screen_name= text
#                 id_User, integer
#                 followers_count integer,
#                 id_Tweet integer,
#                 Tweet text, 
#                 retweet_count integer,
#                 favorite_count integer,
#                 lang text,
#                 hastags text
#                 count+=1
#                 
#                 print(count)
#                 print("--------------------------------------------------------------------------------")
##                 print(type(lista))
                 if count == 10:
                     break
#                 
#    with open('trendsinfo.json', "w+") as json_file:
#             json.dump((lista), json_file, indent=2, ensure_ascii=False)   
             
             
#             with open('data.json', 'w') as outfile:
#    json.dump(az_reviews, outfile, indent=2, ensure_ascii=False) 
#    except:
#        pass
                
#    with codecs.open("trendsinfo.txt", 'w', encoding='utf8') as f:
#          f.write(str(lista)) REVISAR SI DEVUELVE UNA LISTA VACIA O NO WTFFFFF
#    print("lista antes de with open es: {0}".format(lista))      
    
                 

def following():
    with open("trendsinfo.json", "rb") as json_file:
         info=json.load(json_file)  
#         print(type(info))


#        python_dict = json.loads('{"a": 1}'
#        my_string = "{'key':'val','key2':2}"
#        my_dict = ast.literal_eval(my_string)
#         info=json.load(json_file) 
#     count="0"
#     for tweets in info:
#         print((info[count]))
#         count+=1
#         if count==3:
#             break
         
         
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
                 
                     
                     



trendingtweets()  
#log.log(a)
#lookingforplaces()
## 
#searchs()