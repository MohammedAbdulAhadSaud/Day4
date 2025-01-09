try:
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("orange")
except:
    print("Something went wrong")
finally:
     print("The 'try except' is finished")
     print(thislist)
