import datetime


class Inventory:
    def __init__(self,amount):
        self.amount =amount

    def get(self):
        return self.amount >50

class Payment:
    def __init__(self,amount):
        self.amount =amount

    def get(self):
        if self.amount >50 :
            return True
        else:
            return False
class EmailService:
    def __init__(self,name):
        self.name = name

    def get(self,amount):
        print(f"Name: {self.name} | Amount: {amount}")
class Logger:
    def get(self):
        print(datetime.datetime.now())

class OrderFacade:
    def __init__(self,amount,name):
        self.amount = amount
        self.name = name
        self.inventory =Inventory(self.amount)
        self.payment = Payment(self.amount)
        self.emailService = EmailService(name)
        self.logger = Logger()
    def place_order(self):
        print("hello......")
        print(self.payment.get())
        if not self.inventory.get() :
            print("not enough money")
        print(self.inventory.get())
        self.logger.get()
        self.emailService.get(self.amount)
        print("goodby.....")

a = OrderFacade(60,'amirali')
a.place_order()