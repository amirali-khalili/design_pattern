from abc import ABC, abstractmethod


# Implementation
class Serve(ABC):
    @abstractmethod
    def serve(self):
        pass


class Cup(Serve):
    def serve(self):
        return "cup serve.."


class Bottle(Serve):
    def serve(self):
        return "Bottle serve.."


class TakeAway(Serve):
    def serve(self):
        return "TakeAway serve.."


# Abstraction
class Panos(ABC):
    def __init__(self, sarve: Serve):
        self.sarve = sarve

    @abstractmethod
    def tea(self):
        pass


class Coffee(Panos):
    def tea(self) -> int:
        return f"cofe  serve : {self.sarve.serve()}"


class Tea(Panos):
    def tea(self):
        return f"Tea  serve : {self.sarve.serve()}"


class Smoothie(Panos):
    def tea(self):
        return f"Smoothie  serve : {self.sarve.serve()}"


co = Coffee(Bottle())
print(co.tea())
