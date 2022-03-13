from Stack import *
from Queue import *

c = 'Y'
ch = str(input('1.Stack Operation \n2.Queue Operation \n3.Exit \n'))
if ch == "1":
    stack = Stack()
    while c == 'Y':
        a = int(input('1.Push() \n2.Pop() \n3.Display() \n4.Exit \n'))
        if a == 1:
            stack.push()
        elif a == 2:
            stack.pop()
        elif a == 3:
            stack.display()
        elif a == 4:
            exit()
        c = input('Want To Continue in Stack:(Y/N) ')

elif ch == "2":
    queue = Queue()
    while c == 'Y':
        a = str(input('1.Insert() \n2.Delete() \n3.Display() \n4.Exit \n'))
        if a == "1":
            queue.enqueue()
        elif a == "2":
            queue.dequeue()
        elif a == "3":
            queue.display()
        elif a == "4":
            exit()
        c = input('Want To Continue in Queue:(Y/N)')

elif ch == "3":
    exit()