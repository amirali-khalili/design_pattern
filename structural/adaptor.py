from abc import ABC, abstractmethod


class OlsSiste:
    def make_transaction(self, value):
        print(f"pardakht ghadimi {value}")


class NewSistem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class AdaptorOld(NewSistem):
    def __init__(self, old_sistem: OlsSiste):
        self.old_sistem = old_sistem

    def process_payment(self, amount):
        self.old_sistem.make_transaction(amount)


a = AdaptorOld(OlsSiste())
a.process_payment(200000)
