print("*****MENU*****")
choice = input("ENTER YOUR CHOICE: \n1.READ THE CONTENT OF FILES \n2.Copy the contents in another file\
 \n3.ENTER MORE DATA TO THE FILE \n4.CALCULATE NUMBER OF LINES,WORDS,CHARACTERS IN FILE \n5. DISPLAY \
CURRENT DIRECTORY")
if choice=="1":
    print("READING THE FILE WE GET:")
    f1 = open("name.txt","r")
    print(f1.read())

if choice=="2":
    import shutil  #THIS MODULE HELPS FOR COPYING,MOVING,REMOVING FILES
    shutil.copyfile("name.txt","new.txt") #(name of old file,name of new file)
    f2 = open("new.txt","r")
    print(f2.read())

if choice=="3":
    app = input("ENTER A NAME!")
    f1 = open("name.txt","a")
    f1.write(app+ "\n" ) #\n is used so the string gets appended in new line
    f1 = open("name.txt", "r")
    print(f1.read())

if choice=="4":
    f1 = open("name.txt", "r")
    lines = 0
    words = 0
    characters = 0
    for i in f1:
        separate = i.split() #split is used to separate words in a line
        lines = lines + 1
        words = words + len(separate)
        characters = characters + len(i)
    print("THE NUMBER OF LINES ARE:")
    print(lines)
    print("THE NUMBER OF WORDS ARE:")
    print(words)
    print("THE NUMBER OF CHARACTERS ARE:")
    print(characters)

if choice=="5":
    import os
    print("DISPLAYS CURRENT DIRECTORY:")
    print(os.getcwd())
    print("DISPLAYS FILE AVAILABLE IN CUREENT DIRECTORY:")
    print(os.listdir())



