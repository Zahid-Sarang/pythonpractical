
####### LIST ########
l=[] #an empty list
l1=list() #an empty list
l=[10,20,30,40] #an empty list
ch='y'
while ch=='y' or ch=='Y':
    l1.append(int(input('Enter a number: ')))
    ch=input('DO you want to add more? (y/n): ')
print(l1)

print('Reverse is',l1[::-1])
print('Sorted List is',sorted(l1))


####### SET ########

s=set()
st={}
s1={1,2,3,4,5,6}
s2={10,20,30,40,6}
s3={10,20,30,40,6,50,100}
print('Union is ',s1.union(s2))
print(s1.intersection(s2))
# intersection - any common value in two sets
print(s2.issubset(s3))


####### TUPLE ########

t=()
t1=tuple()

t1=(1,2,3,'bushra',1.1)
print(t1.count(1))
print('Help on tuple class: ',dir(tuple()))

####### DICTIONARY ########

d={}
d1=dict()
d2={1:'apple',2:"mango",3:"cherry"}
d2.update({4:'banana'})
print(d2)
l=list(d2.items())
for i in l:  
    print(l)
print(d2.keys())
print(d2.values())

