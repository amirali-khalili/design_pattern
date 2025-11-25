class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        # print("hello")
        return super().__call__(*args, **kwargs)


class Singleton1(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


class child(Singleton1):
    pass


s1 = Singleton1("ali")


class mmm:
    def __call__(self):
        print("hello")


class lll(mmm):
    def __init__(self, name):
        self.name = name


class child(Singleton1):
    pass


s1 = lll("ali")


class Meta(type):
    def __new__(cls, name, bases, dct):
        # print("Meta.__new__ صدا زده شد")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Meta):
    def __init__(self):
        print("MyClass.__init__ صدا زده شد")


# print(type(Singleton1))


class Meta(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwds)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=Meta):
    pass


class Test(Singleton):
    def __init__(self, data):
        self.data = data


a = Test([1, 2, 3])
print(a.data)  # [1, 2, 3]
b = Test([1, 2, 4])
print(a.data)  # [1, 2, 3]
