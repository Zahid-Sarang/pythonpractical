list = [1,2,5,4,0,6,8,9,10]

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

a = [1,2,3,4]
b = [12,19,43,21]
print("THE LIST AFTER MERGED IS")      
print(a+b)

print("THE SORTED LIST IS")
list.sort()
print(list)

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

mx=max(list)
mn=min(list)
print("THE MINIMUM ELEMENT IS")
print(mn)
print("THE MAXIMUM ELEMENT IS")
print(mx)


name = input("ENTER A NAME")
list.append(name)
if (name =="PYTHON"):
    print("WORD PYTHON IS PRESENT")
else:
    print("NOT PRESENT")
print(list)

    
    
        
    
        
