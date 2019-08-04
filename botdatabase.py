# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:42:48 2019

@author: Inki
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
from chatterbot.conversation import Statement

chatbot = ChatBot(
        'AlphaBot',
      storage_adapter='chatterbot.storage.SQLStorageAdapter',
      database_uri='sqlite:///database.sqlite3',
      logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
#        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
#
)

