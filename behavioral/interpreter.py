class Expression:
    def interpret(self):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()
expr = Add(Number(5), Number(3))
print(expr.interpret())    
expr = Subtract(Number(10), Number(4))
print(expr.interpret())    
