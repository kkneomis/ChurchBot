from GroupMeInterface import GroupMeInterface
import json

class Jarvis:
    def __init__(self, logger):
        self.logger = logger
        
    def postLink(self, link):
        self.Speak(link)

    def Speak(self, text):
        GroupMeInterface.SendMessage(text)
        
    