#                        log.log("Valor para seguir a {0} es {1}".format(valor, tweets.user.screen_name))
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:35:07 2019

@author: Inki
"""

import logging 

#logging.basicConfig(handlers=[logging.FileHandler('log.txt', 'w', 'utf-8')], format="%(asctime)s:%(message)s")

logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s:%(message)s")

def log(something):
    try:
        logging.info(something)
    except:
        print("error evitado...")