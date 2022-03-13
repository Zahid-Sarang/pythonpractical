number = 7
print("GUESS THE NUMBER FROM 1 to 10")
class Error(Exception): #MAIN CLASS SINCE ERROR WILL BE PASSED IN EXCEPT
    pass
class ValueTooSmallError(Error):  #CREATING OUR OWN ERRORS!
    pass
class ValueTooLargeError(Error):
    pass #Pass is used since we only want to define error not any other command , It is null operation
while True:
    try:
        n1 = int(input("ENTER A NUMBER"))
        if n1<number:
            raise ValueTooSmallError  #THIS ERROR IS NOT DEFINED INBUILT IN PYTHON,WE CREATED IT!
        elif n1>number:
            raise ValueTooLargeError  #THIS TOO WE DEFINED NEW ERROR
        break
    except ValueTooSmallError:
        print("THIS VALUE IS TOO SMALL")
    except ValueTooLargeError:
        print("THIS VALUE IS TOO LARGE")
    finally:   #THIS WILL ALWAYS PRINT NO MATTER WHAT!
        print("GOOD TRY!")
print("CONGRATULATIONS BUDDY YOU GUESSED IT RIGHT!")

