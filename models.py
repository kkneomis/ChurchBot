from GroupMeInterface import GroupMeInterface
import json

class Bot:
    
    def __init__(self, logger, apikey):
        self.logger = logger
        self.apikey = apikey
        
    def speak(self, link):
        self.dispatch(link)

    def dispatch(self, text):
        GroupMeInterface.SendMessage(text, self.apikey)
        



        