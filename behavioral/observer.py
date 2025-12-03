from abc import ABC, abstractmethod



class Subject:
    def __init__(self,price):
        self._observers = []
        self.price =price
        

    def add_observer(self,observer):
        self._observers.append(observer)
    def delete_observer(self,observer):
        self._observers.remove(observer)

    def add_price(self,price):
        self.price = price
        print(f"{price} jadid sabt shod...")
        for x in self._observers:
            x.update(self.price)


class Observer(ABC):
    @abstractmethod
    def update(self,price):
        pass


class EmailNotifier(Observer):
    def update(self,price):
        print(f"EMAIL :{price}")


class SMSNotifier(Observer):
    def update(self,price):
        print(f"SmS :{price}")


class Logger(Observer):
    def update(self,price):
        print(f"log :{price}")

s = Subject(0)
s.add_observer(EmailNotifier())
s.add_observer(SMSNotifier())
s.add_observer(Logger())
s.delete_observer(EmailNotifier())
s.add_price(200)