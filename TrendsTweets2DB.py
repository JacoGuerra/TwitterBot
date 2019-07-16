# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:56:51 2019

@author: Inki
"""

import tweepy
import keys
import log
from datetime import date
import sqlite3

auth = tweepy.OAuthHandler(keys.Consumer_Key_Following, keys.CONSUMER_SECRET_Following)
auth.set_access_token(keys.ACCESS_KEY_Following, keys.ACCESS_SECRET_Following)
api = tweepy.API(auth, wait_on_rate_limit=True)
#
#auth = tweepy.OAuthHandler(keys.Consumer_Key_Trends, keys.CONSUMER_SECRET_Trends)
#auth.set_access_token(keys.ACCESS_KEY_Trends, keys.ACCESS_SECRET_Trends)
#api = tweepy.API(auth, wait_on_rate_limit=True)

auth1 = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth1.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
api1 = tweepy.API(auth1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


"""
t = twitter.Api(
    consumer_key=e["CONSUMER_KEY"],
    consumer_secret=e["CONSUMER_SECRET"],
    access_token_key=e["ACCESS_TOKEN"],
    access_token_secret=e["ACCESS_TOKEN_SECRET"],
    sleep_on_rate_limit=True
)"""

#timeframe =  date.today()
sql_transaction = []

connection = sqlite3.connect('TweetsCompilation.db')
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Tweets (
                     Screen_name text,
                     Followers_count text,
                     User_id text,
                     Tweet_text text,
                     Hastags text,
                     Tweet_id text,
                     Retweet_count text,
                     Favorite_count text,
                     Lang text,
                     Date text)""")


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


    for value in places.values():
         for a in api.trends_place(value):

             for i in a["trends"]:
                 print("for a in api.trends_place(value)", i)
                 a=i["name"]
                 tweet=api.search(a, tweet_mode='extended')
                 try:
                     tweet=tweet.pop()
                 except Exception as e:
                         print(str(e))

                 if 100 < tweet.user.followers_count and not 'media' in tweet.entities and (tweet.lang == "es" or tweet.lang == "en") \
                 and '@' not in tweet.full_text and ' http' not in tweet.full_text:
                     user_name=(tweet.user.screen_name)
                     followers_count=(tweet.user.followers_count)
                     tweet_id=(tweet.user.id)
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
                     a=True
                     """pendient de pruebas para buscar tweets  replies = t.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)"""
#                     for replies in api1.search(q="in_reply_to_status_id" [, geocode ][, lang ][, locale ][, result_type ][, count][, until][, since_id ][, max_id ][,
#include_entities])

                     for full_tweets in tweepy.Cursor(api1.user_timeline,screen_name=tweet.user.screen_name,timeout=999999).items(10):
                           for tweet in tweepy.Cursor(api1.search,q='to:'+tweet.user.screen_name,result_type='recent',timeout=999999, tweet_mode='extended').items(1000):
                            if hasattr(tweet, 'in_reply_to_status_id_str'):
                               for tweet in  tweepy.Cursor(api.search,q='to:'+tweet.user.screen_name,result_type='recent',timeout=999999, tweet_mode='extended').items(1000):
                                  if tweet.in_reply_to_status_id_str==full_tweets.id_str and tweet.favorite_count > 2 and not 'media' in tweet.entities\
                                  and (tweet.lang == "es" or tweet.lang == "en") and ' http' not in tweet.full_text:
                                     reuser_name=(tweet.user.screen_name)
                                     refollowers_count=(tweet.user.followers_count)
                                     retweet_id=(tweet.user.id)
                                     refull_text=(tweet.full_text)
                                     try:
                                         hashtags=tweet.entities["hashtags"][0]["text"]
                                     except:
                                         hashtags= "NoHashtag"
                                     rehashtags = hashtags
                                     retweet_id=(tweet.id)
                                     reretweet_count=(tweet.retweet_count)
                                     refavorite_count=(tweet.favorite_count)
                                     relang=(tweet.lang)
                                     redates=(date.today().strftime("%m/%d/%y"))
                                     print("__________")
                                     print(full_text)
                                     print(refull_text)
                                     print("__________")

                                     UPDATE_Statement = """INSERT INTO Tweets VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(user_name, followers_count, tweet_id, full_text, hashtags, tweet_id,retweet_count, favorite_count, lang, dates)

                                     c.execute(UPDATE_Statement)
                                     connection.commit()

                                     UPDATE_Statement1=("""INSERT INTO Tweets VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");""".format(reuser_name, refollowers_count, retweet_id, refull_text, rehashtags, retweet_id,reretweet_count, refavorite_count, relang, redates))
                                     c.execute(UPDATE_Statement1)

                                     connection.commit()
                                     a==False


                     if a== True:
                         print("No replies!")
                         print(full_text)
                         print("_____________")

                     UPDATE_Statement = """INSERT INTO Tweets VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(user_name, followers_count, tweet_id, full_text, hashtags, tweet_id,retweet_count, favorite_count, lang, dates)

                     c.execute(UPDATE_Statement)


                     connection.commit()



    c.close()
    connection.close()


    c.close()
    connection.close()


#
#
#def following():
#    with open("trendsinfo.json", "rb") as json_file:
#         info=json.load(json_file)
#         print(type(info))
#
#
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
#
#
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
#





trendingtweets()
#log.log(a)
#lookingforplaces()
##
#searchs()