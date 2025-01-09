#All depertment code....
import it_module1 as it
import cse_module2 as cse
print("From all depertment")
print(it.it_student1)
print(cse.cse_student1)

#College Package
import alldept_subpackage as alldept
print("From Collage")
print(alldept.it.it_student1)
print(alldept.cse.cse_student1)
# cse depertment all code goes here
cse_student1={
 "name":"Md Saad",
 "rollno":501,
 "department":"CSE",
 "percent":94.2
 }
cse_student2={
 "name":"Rahul",
 "rollno":502,
 "department":"CSE",
 "percent":83
 }
# It depertment all code goes here
it_student1={
 "name":"Md Saad",
 "rollno":501,
 "department":"IT",
 "percent":90.9
 }
it_student2={
 "name":"Rahul",
 "rollno":502,

 "department":"IT",
 "percent":85.5
 }
#Admin Code
import sys
sys.path.insert(0, '../python/collage') #setting packages path
import collage_package as collage
print("From collage")
print(collage.alldept.it.it_student1)
print(collage.alldept.cse.cse_student1)
