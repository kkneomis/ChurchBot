import requests

class GroupMeInterface:
    @staticmethod
    def SendMessage(message, apikey):
        url = "https://api.groupme.com/v3/bots/post"
        r = requests.post(url, {"text" : message, "bot_id" : apikey}) #test group
        #r = requests.post(url, {"text" : message, "bot_id" : "14ce03538d7f2509f9910434ee"}) #emerging coders
        print r.status_code