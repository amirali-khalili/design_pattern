import time
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.handler = None
    def set_next_handler(self, handler):
        self.handler = handler
        return handler

    @abstractmethod
    def handle(self,request):
        if self.handler is not None:
            return self.handler.handle(request)
        return True

class NotEmptyHandler(Handler):
    def handle(self, request):
        if request == '':
            return "Empty request...!"
        else:
            print("part 1 done..")
            return super().handle(request)
            

class MinLengthHandler(Handler):
    def handle(self, request):
        if len(request) <5:
            return "Not enough"
        else:
            print("part 2 done..")
            return super().handle(request)
class NoAtHandler(Handler):
    def handle(self, request):
        if '@' in request:
            return "not...."
        else:
            print("part 3 done..")
            return super().handle(request)


class ViewHandler(Handler):
    def __init__(self, view_func):
        super().__init__()
        self.view_func = view_func

    def handle(self, request):
        return self.view_func(request)

def test_view(request):
    print("View executed!")
    print(f"Request length: {len(request)}")
    print(f"Time: {time.time()}")
    return f"Response for '{request}'"

a1=NotEmptyHandler()
a2=MinLengthHandler()
a3=NoAtHandler()
view = ViewHandler(test_view)

a1.set_next_handler(a2).set_next_handler(a3).set_next_handler(view)

print(a1.handle("aliiii"))