from abc import ABC

class Dish(ABC):
    def prepare_dish(self):
        self.mavad_avale()
        self.pokht()
        self.serve()   
    
    def mavad_avale(self):
        print("dare mavad avalie..")
    
    def pokht(self):
        print("dare mipaze..")
    
    def serve(self):
        """Hook: optional, can be overridden"""
        pass

class Pizza(Dish):
    def pokht(self):
        print("pitza")
        super().pokht()
    
    def serve(self):
        print("serv pizza")

class Soup(Dish):
    def serve(self):
        print("serv soup")

class Salad(Dish):
    pass

p = Pizza()
p.prepare_dish()

s = Soup()
s.prepare_dish()

sal = Salad()
sal.prepare_dish()
