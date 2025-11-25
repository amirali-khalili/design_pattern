from abc import ABC, abstractmethod


# --------main class----------
class Food(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def prepare(self):
        pass


class Pitza(Food):
    def prepare(self):
        print(f"oh pitza....{self.price}")


class salad(Food):
    def prepare(self):
        print(f"oh salad....{self.price}")


class Burger(Food):
    def prepare(self):
        print(f"oh Burger....{self.price}")


# ________crator class_________
class FoodCreator(ABC):
    @abstractmethod
    def crate_food(self):
        pass

    def show(self):
        a = self.crate_food()
        return a.prepare()


class PitzaCreator(FoodCreator):
    def crate_food(self):
        amount = input("your amount :")
        return Pitza(amount)


class saladCreator(FoodCreator):
    def crate_food(self):
        amount = input("your amount :")
        return salad(amount)


class BurgerCreator(FoodCreator):
    def crate_food(self):
        amount = input("your amount :")
        return Burger(amount)


class FoodFactory:
    types = {
        "pitza": PitzaCreator(),
        "Salad": saladCreator(),
        "Burger": BurgerCreator(),
    }

    @classmethod
    def factory_food(cls, typeu):
        if typeu not in cls.types:
            print("ridi...")
        instane = cls.types[typeu]
        return instane.show()


ix = input("your food :")
FoodFactory.factory_food(ix)
