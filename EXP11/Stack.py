class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0
        self.max = 100

    def push(self):
        if self.top == self.max:
            print('Stack Overflow')
        else:
            x = str(input('Enter Element:'))
            self.stack.append(x)
            print('Element Entered', x)
            self.top = self.top + 1

    def pop(self):
        if self.top == 0:
            print('Stack Underflow')
            return None
        else:
            self.stack.pop()
            print('Element Removed')
            self.top = self.top - 1

    def display(self):
        print('Stack Elements Are:')
        print(self.stack)

