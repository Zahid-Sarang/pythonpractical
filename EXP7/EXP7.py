class Employee():
    empCount = 0

    def __init__(self, eid, name, salary, yr):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.yr = yr
        Employee.empCount += 1
     
    def displayEmployee(self):
        print ("eid : ", self.eid,", Name : ", self.name,  ", Salary: ", self.salary,  ", yr: ", self.yr)
emp1 = Employee(1,"Santosh", 2000,10)
emp2 = Employee(2,"Apoorva", 4000,20)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
