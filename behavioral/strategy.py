# CreditCardPayment	شماره کارت، CVV، تاریخ انقضا دریافت کند
# PayPalPayment	ایمیل کاربر دریافت کند
# CryptoPayment	آدرس کیف پول دریافت کند

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self):
        self.number = input("number :")
        self.CVV = input("CVV :")
        self.tarikh = input("tarikh :")

    def pay(self,amount):
        print(F"mablagh {amount} pardekht az {self.number} ba {self.CVV} ta {self.tarikh} anjam shod...")

class PayPalPayment(PaymentStrategy):
    def __init__(self):
        self.email = input("email :")
    def pay(self,amount):
        print(f"mablagh {amount} parakht PayPalPayment = {self.email}")
class CryptoPayment(PaymentStrategy):
    def __init__(self):
        self.adress = input("adress :")
    def pay(self,amount):
        print(f"mablagh {amount} parakht PayPalPayment = {self.adress}")

class PaymentContext:
    def __init__(self,strategy):
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy
    @strategy.setter
    def strategy(self,strategy):
        self.__strategy = strategy
    def pay(self,amount):
        return self.__strategy.pay(amount)
    

a = PaymentContext(CreditCardPayment())
a.pay(250)
a = PaymentContext(PayPalPayment())
a.pay(500)
a = PaymentContext(CryptoPayment())
a.pay(100)