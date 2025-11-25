import copy


class MyClass:
    def __init__(self, data):
        self.data = data

    def __copy__(self):
        print("------shalow Copy-------")
        return MyClass(copy.copy(self.data))

    def __deepcopy__(self, memo):
        print("------deep Copy-------")
        return MyClass(copy.deepcopy(self.data, memo))


a1 = MyClass([1, 2, 3, [5, 6]])
print(a1.data)
a2 = copy.copy(a1)
a2.data.append(20)
print(a2.data)
a2.data[3].append(4)
print(a2.data)
print("a 1")
print(a1.data)
a3 = copy.deepcopy(a1)
a3.data.append(7)
a3.data[3].append(500)
print(a3.data)
print("a 1")
print(a1.data)
