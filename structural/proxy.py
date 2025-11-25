import time
from abc import ABC, abstractmethod


class BaceProduct(ABC):
    def __init__(self, price):
        self.price = price

    def show_price(self):
        pass


class Product(BaceProduct):
    def show_price(self):
        print(self.price)


class ProductProxy(BaceProduct):
    def __init__(self, price, user):
        super().__init__(price)
        self.user = user

    def show_price(self):
        if self.user["VIP"] == False:
            print(f"{self.price} = 20 taman azash kam mishe --> {self.price - 20}")

        else:
            print(self.price)


user1 = {"NAME": "ALI", "VIP": True}
user2 = {"NAME": "AHMAD", "VIP": False}
product1 = ProductProxy(20000, user1)
product2 = ProductProxy(170, user2)

product3 = Product(20000)
product3.show_price()

product1.show_price()
product2.show_price()


class RealService:
    def process(self):
        time.sleep(1.5)
        print("RealService processing...")


class ProxyService(RealService):
    def process(self):
        a = time.time()

        print("LOG before process")
        time.sleep(2)
        super().process()
        print("LOG after process")
        b = time.time() - a
        print("all time ==>", round(b, 1), "s")


proxy = ProxyService()
proxy.process()
