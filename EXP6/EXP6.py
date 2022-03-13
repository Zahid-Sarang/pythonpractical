print("****MENU****")
choice=input("ENTER YOUR CHOICE:\n1.CREATE A DICTONARY\n2.UPDATE AND DELETE ITEMS IN A DICTONARY\n.3.DISPLAY VALUE FROM A KEY \n4.MAP TWO LIST")
if choice=="1":
    dict0={}
    key=input("ENTER THE KEY:")
    value=input("ENTER THE VALUE")
    dict0[key]=value
    print(dict0)
if choice=="2":
    dict2={}
    dict1={"BOND":"007","TANAY":"020","SMOL":"30"}
    print("BEFORE UPDATION AND DELETION:")
    print(dict1)
    #UPDATION
    key2=input("ENTER YOUR NAME:")
    value2=input("ENTER YOUR FAV NO:")
    dict2[key2]=value2
    dict1.update(dict2)
    print("AFTER UPDATION:")
    print(dict1)
    #DELETION
    delete=input("ENTER THE NAME TO BE DELETED")
    del dict1[delete]
    print("AFTER DELETION:")
    print(dict1)
if choice=="3":
    dict3={"bond":"007","TANAY":"002","AMOl":"16"}
    print(dict3.key())
    find=input("ENTER THE KEY FROM ABOVE TO FIND ITS VALUE:")
    print("VALUE FROM A KEY IS:")
    print(dict3[find])
if choice=="4":
    Name=["santosh","apoorva","deepesh","soham","amol"]
    Roll=["002","8","16","30"]
    print("THE ORGINAL 1st LIST IS:")
    print(Name)
    print("THE ORGINAL 2nd LIST IS:")
    print(Roll)
    Map=dict(zip(Name,Roll))
    print("AFTER MAPPING TWO LIST TO DICTONARY:")
    print(Map)
