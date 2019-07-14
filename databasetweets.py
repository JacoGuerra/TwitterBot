# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:01:45 2019

@author: Inki
"""

#building a database

import sqlite3
                
#timeframe =  date.today()
sql_transaction = []
start_row = 4000000
cleanup = 16000000

connection = sqlite3.connect('trendstweets.db')
c = connection.cursor() 
   
def create_table():
    c.execute("""CREATE TABLE Tweets (
                     Screen_name text,
                     Followers_count text,
                     User_id text,
                     Tweet_text text,
                     Hastags text,
                     Tweet.id text,
                     Retweet_count text,                   
                     Favorite_count text,
                     Lang text,
                     Date text
            )""")       
    
    connection.commit()
    
    connection.close()

      
                 