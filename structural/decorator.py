from abc import ABC, abstractmethod


def decorat(func):
    def wrapper(self, *args, **kwargs):
        return func(self,*args, **kwargs) + 3
    return wrapper


class Cofe(ABC):
    @abstractmethod
    def operator(self):
        pass

class Coffee(Cofe):
    def operator(self):
        return 5
class MilkDecorator:
    def __init__(self,coffee):
        self.coffee = coffee

    def operator(self):
        return self.coffee.operator() + 2
class SugarDecorator:
    def __init__(self,coffee):
        self.coffee = coffee

    @decorat
    def operator(self):
        return self.coffee.operator() + 1


a = Coffee()
print(a.operator())
b = MilkDecorator(a)
print(b.operator())
c = SugarDecorator(b)
print(c.operator())


