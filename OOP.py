class Robot:
    def __init__(self,name,owner="Elon Musk"):
        self.model = "XUI876"
        self.language = "Python"
        self.name = name
        self.owner = owner
    def speak(self):
        print("Hello I am", self.name,"and my owner is",self.owner)

    def set_friend(self,friend_object):
        self.friend = friend_object
        friend_object.friend = self

sophia = Robot("Sophia")
alexa = Robot("Alexa",owner="Jeff Bezos")
#print(sophia.model)
sophia.set_friend(alexa)
#print("Hey I am", sophia.name,"My friend is ",sophia.friend.name)
#print("Hey I am",alexa.name,"My friend is", alexa.friend.name)
#print(alexa.model, alexa.language, alexa.name, alexa.owner)
#sophia.speak()
#alexa.speak()

from datetime import datetime

class Chatbot(Robot):
    def time(self):
        today = datetime.now()
        print(today.strftime("Date:: %d-%m-%y Time:: %H:%M:%S"))

apple = Chatbot("Siri")
print(apple.owner)
apple.speak()
apple.time()
