# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:11:16 2019

@author: Inki
"""
import log
import randomposting
import retweets
#import replier
import following
#import remove

#parar =remove.remove()
#parar.start()

log.log("INICIANDO.......................................")

postear=randomposting.randomposting()
postear.start()  
#
reposts=retweets.retweets()
reposts.start()
###
#responder=replier.replier()
#responder.start()

seguir=following.following()
seguir.start()

