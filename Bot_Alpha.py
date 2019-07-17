# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 00:48:48 2019

@author: Inki
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
from chatterbot.conversation import Statement

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('Export Example Bot',
      storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
#        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
#    database_uri='sqlite:///database.sqlite3'
)

## First, lets train our bot with some data
#trainer = ChatterBotCorpusTrainer(chatbot)
#
#trainer.train('chatterbot.corpus.english')
#
## Now we can export the data to a file
#trainer.export_for_training('./my_export.json')



def get_feedback():

    text = input()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()

while True:
    try:
        input_statement = Statement(text=input())
        response = chatbot.generate_response(
            input_statement
        )

        print('\n Is "{}" a coherent response to "{}"? \n'.format(
            response.text,
            input_statement.text
        ))
        if get_feedback()== False:
            print('please input the correct one')
            correct_response = Statement(text=input())
            chatbot.learn_response(correct_response, input_statement)
            print('Responses added to bot!')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


