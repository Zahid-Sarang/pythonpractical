list = [1,2,5,4,0,6,8,9,10]
choice = input("ENTER YOUR CHOICE: 1.PUT EVEN AND ODD NUMBERS IN DIFFERENT LIST \n2.MERGE AND SORT\
INTO TWO LISTS \n3.UPDATE FIRST ELEMENT AND DELETE MIDDLE ELEMENT \n4.\
IND MAX & MIN ELEMENT \n5.ADD NAMES AND CHECK IF PYTHON NAME IS PRESENT")

if choice==1:
    evenlist = []
    oddlist = []
    for i in list:
        if (i%2==0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("THE EVEN LIST IS")
    print(evenlist)
    print("THE ODD LIST IS")
    print(oddlist)

if choice==2:
    a = [1,2,3,4]
    b = [12,19,43,21]
    print("THE LIST AFTER MERGED IS")
    print(a+b)
    print("THE SORTED LIST IS")
    list.sort()
    print(list)

if choice==3:
    first = int(input("ENTER ELEMENT TO BE INSERTED FIRST"))
    print("BEFORE  THE UPDATION")
    print(list)
    list[0] = first
    print("AFTER THE UPDATION")
    print(list)
    c = len(list)
    print(c)
    mid =(0+(c-1))//2
    print("THE DELETED LIST IS")
    del list[mid]
    print(list)

if choice==4:
    mx=max(list)
    mn=min(list)
    print("THE MINIMUM ELEMENT IS")
    print(mn)
    print("THE MAXIMUM ELEMENT IS")
    print(mx)

if choice==5:
    list.append("C")
    list.append("JAVA")
    list.append("PYTHON")
    list.append("R")
    list.append("C++")
    list.append("SQL")
    for i in list:
        if (i == "PYTHON"):
            print("WORD PYTHON IS PRESENT")
    print("THE LIST AFTER ADDING NEW ELEMENTS IS:")
    print(list)
