'''
To implement comments,datatypes,expression,input and output functions.
Title of my progrm
            @author
           Khan Bushra Sarfaraz
           21DCO04
           2021-22

    Theory about the underlying concept of the program        

Comments:A comment in Python starts with the hash character, # , and extends to the end of the physical line. A hash character within a string value is not seen as a comment, though. To be precise, a comment can be written in three ways - entirely on its own line, next to a statement of code, and as a multi-line comment block.

DATATYPE: In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

Expression: An expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operators.
'''

i=10
print("Data =",i,"and it's type is",type(i),"and it's location will be",id(i))

x=20.0
print("Data =",x,"and it's type is",type(x),"and it's location will be",id(x))

y="aiktc"
print("Data =",y,"and it's type is",type(y),"and it's location will be",id(y))

var = int(input("Enter your data:"))
print("Scanned data is ",var,".","and data type is",type(var),sep="")

#indentation

a = int(input("Enter your data:"))
b = int(input("Enter your data:"))
c = int(input("Enter your data:"))

if a > b and a > c :
    print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")
    
'''
Output:

PS D:\python_sem4> python -u "d:\python_sem4\Exp101.py"

Data = 10 and it's type is <class 'int'> and it's location will be 140710037952448
Data = 20.0 and it's type is <class 'float'> and it's location will be 2663598879824
Data = aiktc and it's type is <class 'str'> and it's location will be 2663600907504
Enter your data:100
Scanned data is 100.and data type is<class 'int'>
Enter your data:200
Enter your data:300
Enter your data:400
c is greater


Conclusion: We have learned to implement comments,datatypes,expression,input and output functions.
'''