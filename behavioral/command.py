from abc import ABC,abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class LightOff(Command):

    @staticmethod
    def execute():
        print("light off")
    def undo(self):
        return LightOn.execute()
class LightOn(Command):
    @staticmethod
    def execute():
        print("light on")
    def undo(self):
        return LightOff.execute()
#  Command
class SendEmailCommand(Command):
    def __init__(self,email, text):
        self.resever = EmailReceiver()
        self.email = email
        self.text = text
    def execute(self):
        return self.resever.send_email(self.email, self.text)

class ResizeImageCommand(Command):
    def __init__(self,filename, width, height):
        self.resever=ImageReceiver()
        self.filename = filename
        self.width = width
        self.height = height
    def execute(self):
        return self.resever.resize_image(self.filename, self.width, self.height)

class GenerateReportCommand(Command):
    def __init__(self,report_type):
        self.resever=ReportReceiver()
        self.report_type = report_type
    def execute(self):
        return self.resever.generate_report(self.report_type)

#Resever
class EmailReceiver:
    def send_email(self,email,text):
        print(f"Sending email to {email} with text {text}")

class ImageReceiver:
    def resize_image(self,filename, width, height):
        print(f"Resizing image to {width}x{height} with filename {filename}")

class ReportReceiver:
    def generate_report(self,report_type):
        print(f"Generating report for {report_type}")

# Invoker

class TaskQueue:
    def __init__(self):
        self.commands = []
    def add(self,command):
        self.commands.append(command)
    def run(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()
        print(self.commands)


queue = TaskQueue()

queue.add(SendEmailCommand("ali@test.com", "Hello Ali!"))
queue.add(ResizeImageCommand("pic.jpg", 200, 200))
queue.add(GenerateReportCommand("sales"))

queue.run()

class TaskLight:
    def __init__(self):
        self.commands = []
    def add(self,command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()
    def undo(self):
        for command in self.commands:
            command.undo()

a =TaskLight()
a.add(LightOff())
a.add(LightOn())
a.run()
a.undo()