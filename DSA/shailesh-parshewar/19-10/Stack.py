
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) < 1:
            self.stack = []
        else:
            self.stack = self.stack[:-1]


