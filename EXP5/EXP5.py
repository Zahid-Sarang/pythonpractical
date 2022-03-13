s=input("ENTER YOUR NAME:")
d=input("ENTER YOUR FRIEND'S NAME:")
set1 = set(list(s))
set2 = set(list(d))
print("*******MENU*******")
choice = input("ENTER YOUR CHOICE:\n1. DISPLAY COMMON LETTERS FROM THE NAME \n2.DISPLAY LETTER PRESENT IN ONLY YOUR NAME\n3.DISPLAY ALL LETTER PRESENT IN NAME\n4.DISPLAY UNCOMMON LETTER IN THE NAME\n")
if choice == "1":
    print(set1.intersection(set2))
if choice == "2":
    print(set1.difference(set2))
if choice == "3":
    print(set1|set2)
if choice == "4":
    print(set1.symmetric_difference(set2))

