# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 01:04:18 2019

@author: Inki
"""
import sys
from threading import Thread

class remove(Thread):
    def run(self):
        self.remove()
        
    def remove(self):
        while True:
            request=input("Puls x para parar")
            if request == "x":
                break
            
            
import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()