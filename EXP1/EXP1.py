x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))
x,y=y,x
print("x=",x)
print("y=",y)
if y > 0:
   print(y,"is Positive number")
elif y == 0:
   print(y,"is Zero")
else:
   print(y,"is Negative number")
