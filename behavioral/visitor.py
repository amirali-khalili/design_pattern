from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def prudact(self):
        print( self.name, self.price)

    @abstractmethod
    def acept(self):
        pass


class FoodProduct(Product):
    def acept(self,visitor):
        return visitor.food_visit(self)

class PhysicalProduct(Product):
    def __init__(self,name, price,weight):
        super().__init__(name, price)
        self.weight = weight
    def acept(self,visitor):
        return visitor.physical_visit(self)

class DigitalProduct(Product):
    def acept(self,visitor):
        return visitor.digital_visit(self)

class ProductVisitor(ABC):
    @abstractmethod
    def food_visit(self):
        pass

    @abstractmethod
    def physical_visit(self):
        pass
    @abstractmethod
    def digital_visit(self):
        pass

class PriceCalculatorVisitor(ProductVisitor):
    def food_visit(self,prudact):
        print("malyat : ",prudact.price * 5)
    def physical_visit(self,prudact):
        print("malyat : ",prudact.price +prudact. weight *2)
    def digital_visit(self,prudact):
        print("malyat : ",prudact.price +250)

class ReportVisitor(ProductVisitor):
    def food_visit(self,prudact):
        prudact.prudact()
    def physical_visit(self,prudact):
        prudact.prudact()

    def digital_visit(self,prudant):
         prudant.prudact()

class JsonExportVisitor(ProductVisitor):
    def food_visit(self,product):
        return {
            "type": "food",
            "name": product.name,
            "price": product.price,
        }
    def physical_visit(self,product):
        return {
            "type": "physical",
            "name": product.name,
            "price": product.price,
        }
    def digital_visit(self,product):
        return {
            "type": "digital",
            "name": product.name,
            "price": product.price,
        }

a1= PriceCalculatorVisitor()
a2 =ReportVisitor()
a3 = JsonExportVisitor()

f= FoodProduct("Ford",20000)
f.acept(a1)
f.acept(a2)
print(f.acept(a3))