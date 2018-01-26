import requests

class GroupMeInterface:
    @staticmethod
    def SendMessage(message):
        url = "https://api.groupme.com/v3/bots/post"
        r = requests.post(url, {"text" : message, "bot_id" : "9d2619675f5521bb6ffba65270"}) #test group
        #r = requests.post(url, {"text" : message, "bot_id" : "14ce03538d7f2509f9910434ee"}) #emerging coders
        print r.status_code