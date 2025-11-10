from abc import ABC, abstractmethod
from datetime import datetime

# ---------- Product ----------
class Order:
    def __init__(self):
        self.parts = {}

    def add_part(self, key, value):
        self.parts[key] = value

    def show_info(self):
        print("\n🧾 Order Receipt:")
        for part, value in self.parts.items():
            print(f"{part}: {value}")


# ---------- Abstract Builder ----------
class OrderBuilder(ABC):
    def __init__(self):
        self.order = Order()

    @abstractmethod
    def add_customer(self): pass

    @abstractmethod
    def add_items(self): pass

    @abstractmethod
    def add_payment(self): pass

    @abstractmethod
    def add_summary(self): pass


# ---------- Concrete Builder ----------
class NormalOrderBuilder(OrderBuilder):
    def add_customer(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        self.order.add_part("Customer", f"{name} ({email})")

    def add_items(self):
        items = []
        while True:
            item = input("Enter item name (or 'done' to finish): ")
            if item.lower() == "done":
                break
            qty = input(f"Enter quantity for {item}: ")
            price = input(f"Enter price for {item}: ")
            items.append(f"{item} x{qty}: {price}$")
        self.order.add_part("Items", "\n  ".join(items))

    def add_payment(self):
        payment = input("Enter payment method (Cash/Card/Online): ")
        self.order.add_part("Payment", payment)

    def add_summary(self):
        # فقط یک جمع تقریبی برای نمایش
        self.order.add_part("Total", "calculated in real app")
        self.order.add_part("Date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# ---------- Director ----------
class OrderDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_order(self):
        self.builder.add_customer()
        self.builder.add_items()
        self.builder.add_payment()
        self.builder.add_summary()
        return self.builder.order


# ---------- Run Program ----------
if __name__ == "__main__":
    print("👋 Welcome to Order Builder Program!")
    builder = NormalOrderBuilder()
    director = OrderDirector(builder)
    order = director.build_order()
    order.show_info()
