from GroupMeInterface import GroupMeInterface
import json

class Jarvis:
    def __init__(self, logger):
        self.logger = logger
        self.Speak("Hello everyone! Every sunday I will be posting the link to the hangout.")
        
        
    def Welcome(self, name, body):
        if ("groupme" in name) and ("added" in body):
            self.Speak("Welcome to the group %s!" % name)
        
    def postLink(self, link):
        self.Speak(link)

    def Speak(self, text):
        GroupMeInterface.SendMessage(text)
        
    