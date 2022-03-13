c = input("Enter 1 To Get Number Is palindrome:\nEnter 2 For String palindrome:\nEnter 3 For Factorial:\nEnter 4 For Exit:\n ")
while (c != '1') | (c != '2') | (c != '3')| (c != '4'):
    if c == '1':
        n=int(input("Enter number:"))
        temp=n
        rev=0
        while(n>0):
            a=n%10
            rev=rev*10+a
            n=n//10
        if(temp==rev):
            print("The Number is a palindrome")
        else:
            print("The Number is not palindrome")
            exit(1)

    elif c == '2':
        string=input(("Enter a string:"))
        str1=reversed(string)
        if(list(string)==list(str1)):
            print("The string is a palindrome")
        else:
            print("Not a palindrome")
            exit(1)
    elif c == '3':
        num = int(input("Enter a number: "))  
        factorial = 1  
        if num < 0:  
           print("Sorry, factorial does not exist for negative numbers")  
        elif num == 0:  
           print("The factorial of 0 is 1")  
        else:  
            for i in range(1,num + 1):  
               factorial = factorial*i  
               print("The factorial of",num,"is",factorial)  
    elif c == '4':
        exit(1)




