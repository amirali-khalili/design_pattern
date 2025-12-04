from abc import ABC, abstractmethod

# State 
class State(ABC):
    def __init__(self):
        self.context = None

    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self, pin: int):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def eject_card(self):
        pass

# Concrete State
class CardNotInserted(State):
    def insert_card(self):
        print("Card inserted.")
        self.context.change_state(CardInserted())

    def enter_pin(self, pin: int):
        print("Error: No card inserted!")

    def withdraw(self, amount: float):
        print("Error: No card inserted!")

    def eject_card(self):
        print("Error: No card inserted!")


class CardInserted(State):
    def insert_card(self):
        print("Error: Card already inserted!")

    def enter_pin(self, pin: int):
        if pin == self.context.correct_pin:
            print("PIN correct.")
            if self.context.balance > 0:
                self.context.change_state(Authenticated())
            else:
                self.context.change_state(NoMoney())
        else:
            print("Incorrect PIN!")

    def withdraw(self, amount: float):
        print("Error: Enter PIN first!")

    def eject_card(self):
        print("Card ejected.")
        self.context.change_state(CardNotInserted())


class Authenticated(State):
    def insert_card(self):
        print("Error: Card already inserted!")

    def enter_pin(self, pin: int):
        print("Error: Already authenticated!")

    def withdraw(self, amount: float):
        if amount <= self.context.balance:
            self.context.balance -= amount
            print(
                f"Withdrew ${amount}. Remaining balance: ${self.context.balance}")
            if self.context.balance == 0:
                self.context.change_state(NoMoney())
        else:
            print("Error: Insufficient funds!")

    def eject_card(self):
        print("Card ejected.")
        self.context.change_state(CardNotInserted())


class NoMoney(State):
    def insert_card(self):
        print("ATM is empty! Cannot insert card.")

    def enter_pin(self, pin: int):
        print("ATM is empty! Cannot authenticate.")

    def withdraw(self, amount: float):
        print("ATM is empty! Cannot withdraw.")

    def eject_card(self):
        print("Card ejected.")
        self.context.change_state(CardNotInserted())


# context
class ATM:
    def __init__(self, balance: float, correct_pin: int):
        self.balance = balance
        self.correct_pin = correct_pin
        self.state = CardNotInserted()
        self.state.context = self

    def change_state(self, new_state):
        print(f"\n[STATE] Changing to {type(new_state).__name__}")
        self.state = new_state
        self.state.context = self

    def insert_card(self):
        return self.state.insert_card()

    def enter_pin(self, pin: int):
        self.state.enter_pin(pin)

    def withdraw(self, amount: float):
        self.state.withdraw(amount)

    def eject_card(self):
        return self.state.eject_card()


atm = ATM(balance=100, correct_pin=1234)
atm.insert_card()
atm.enter_pin(1234)
atm.withdraw(50)
atm.withdraw(60)
atm.eject_card()
atm.insert_card()
