 
from abc import ABC
import time


class Mediator(ABC):


    def send(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.users = []

    def send(self, sender, event)  :
        print(f"{event} send az {sender}")
        time.sleep(2)
        print("-----------------------------------")
        for x in self.users :
            if x.name != sender:
                x.receive(sender,event)

    def add_user_active(self,user):
        self.users.append(user)

class BaseComponent(ABC):
    def send(self):
        pass
    def receive(self):
        pass

class User(BaseComponent):
    def __init__(self,mediator,name):
        self.mediator =mediator
        self.name = name

    def send(self,event):
        return self.mediator.send(self.name,event)
    def receive(self,sender,event):
        print(f"{self.name} payam {event} az {sender} omad brat")

m=ConcreteMediator()
a= User(m,"ali")
bahman= User(m,"bahman")
ma= User(m,"majid")
m.add_user_active(a)
m.add_user_active(bahman)
m.add_user_active(ma)
a.send("salammm")