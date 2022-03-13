class Calculation1:  
    def Summation(self,a,b):  
        return a+b  

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b 

class Derived1(Calculation1,Calculation2): #PARENT CLASS FOR MULTIPLE INHERITANCE (P1)
    def Divide(self,a,b):   
        return a/b

class Derived2(Calculation1): #NEW PARENT CLASS HAS BEEN DEFINED FOR SINGLE INHERITANCE (P2)
    def subtract(self,a,b):
        return a-b

#P1
print("MULTIPLE INHERITANCE:")   
d1 = Derived1()  
print(d1.Summation(10,20))  
print(d1.Multiplication(10,20))  
print(d1.Divide(10,20))

#P2
print("SINGLE INHERITANCE:")
d2 = Derived2()
print(d2.Summation(10,10))



