

class Calculator:
    def __init__(self):
        self.current_value=0

    def add(self,number):
        self.current_value += number

    def subtract(self, number):
        self.current_value -= number
    def memento(self):
        return Memento(self.current_value)
    def restore(self,memento):
        self.current_value =memento.current_value
class Memento:
    def __init__(self,current_value):
        self.current_value=current_value

class Caretaker:
    def __init__(self):
        self.undos =[]
        self.redos=[]
    def save(self,memento):
        self.undos.append(memento)
        self.redos.clear()
    def undo(self) :
        if len(self.undos) <= 1:  
            return None
        last = self.undos.pop()
        self.redos.append(last)
        return self.undos[-1]
    def redo(self):
        if self.redos is None:
            return None
        a = self.redos.pop()
        self.undos.append(a)
        return a

h= Caretaker()
a =Calculator()
a.add(5)
h.save(a.memento())
a.add(15)
h.save(a.memento())



m=h.undo()
a.restore(m)

a.add(2)
h.save(a.memento())


print(a.current_value)
print("------------------------")

print("-----redo----")
for x in h.redos:
    print(x.current_value)
print("-----undo-----")
for x in h.undos:
    print(x.current_value)
