class Queue:

    def __init__(self):
        self.queue = []
        self.rear = 0
        self.front = 0
        self.max = 100

    def enqueue(self):
        if self.rear == self.max:
            print('Queue Full')
        else:
            x = str(input('Enter Element: '))
            self.queue.append(x)
            print('Element Inserted', x)

    def dequeue(self):
        if self.front == 0:
            print('Queue Empty')
            return None
        else:
            self.queue.pop(0)

    def display(self):
        print('Queue Elements Are:')
        print(self.queue)