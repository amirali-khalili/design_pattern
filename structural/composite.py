# Component
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

class MenuItem(Component):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("_" * indent + self.name)

class MenuGroup(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self, indent=0):
        print(" " * indent + self.name)
        for item in self.items:
            item.show(indent + 2)


home = MenuItem("Home")
about = MenuItem("About")
contact = MenuItem("Contact")
products = MenuGroup("Products")
products.add(MenuItem("Laptop"))
products.add(MenuItem("Phone"))

services = MenuGroup("Services")
services.add(MenuItem("Consulting"))
services.add(MenuItem("Support"))

main_menu = MenuGroup("Main Menu")
main_menu.add(home)
main_menu.add(products)
main_menu.add(services)
main_menu.add(contact)


main_menu.show()
