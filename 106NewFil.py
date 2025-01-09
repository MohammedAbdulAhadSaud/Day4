#Create a new file
f = open("PLab.txt", "w")
#Write to an Existing File
#Open the file “PPLab.txt", and append content to the file:
f = open("PLab.txt", "a")
f.write("Hello World ! the file has more content!")
f.close()
#open and read the file after the appending:
f = open("PLab.txt", "r")
print(f.read())
f = open("PLab.txt", "r")
#stores all the data of the file into the variable content
content = f.read(4)
# prints the type of the data stored in the file
print(type(content))
#prints the content of the file
print(content)
# Close file
f = open("PLab.txt ", "r")
print(f.readline())
f.close()
f1 = open("PLab.txt","x")
print(f1)
if f1:
 print("File created successfully") 
