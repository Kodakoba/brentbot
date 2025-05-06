import datetime

class Greeting():
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        return f'Hello {name}, i am brent'

    def greet_based_on_input(self, name):
        now = datetime.datetime.now()
        if now.hour < 12:
            return f'Good Morning {name}'
        elif 12 <= now.hour < 18:
            return f'Good Afternoon {name}'
        else:
            return f'Good Evening {name}'

#tbh im writing his file the day before its due, I just need *an* integration test to be honest.