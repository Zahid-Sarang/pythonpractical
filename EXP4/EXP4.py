tup1 = ("santosh", "apoorva", "shivam", "raj")
tup2 = ("61", "53", "60", "50")
tup3 = ("Physics - 90 Chemistry - 80 Maths - 70",
        "Physics - 80 Chemistry - 90 Maths - 80",
        "Physics - 70 Chemistry - 70 Maths - 90",
        "Physics - 60 Chemistry - 60 Maths - 60")
print("""1.Print the Marks
2.Display marks of python
3.demo of nested tuple and sorting of nested tuple""")
a = int(input("Enter Your Choice: "))
if a == 1:
    c = 0
    for b in tup1:
        print(c, b)
        c += 1
    d = input("Enter name: ")
    f = tup1.index(d)
    print(tup1[f], tup2[f], '\n' + tup3[f])
elif a == 2:
    print(tup1[3], tup2[3], '\n' + tup3[3])
elif a == 3:
    for e in tup1:
        e = tup1.index(e)
        tup4 = (tup2[e], tup3[e])
        print(tup4)
        print(sorted(tup4))
