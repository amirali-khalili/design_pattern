class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        print("hello")
        return super().__call__(*args, **kwargs)

class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

class child(Singleton):
    pass

s1 = Singleton("ali")

class mmm:
    def __call__(self):
        print("hello")


class lll(mmm):
    def __init__(self, name):
        self.name = name

class child(Singleton):
    pass

s1 = lll("ali")

class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Meta.__new__ صدا زده شد")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    def __init__(self):
        print("MyClass.__init__ صدا زده شد")


print(type(Singleton))