import sem
import sys
import years
sem1_techers = {
 "techer1" : {
 "name" : "XYZ",
 "year" : 2000
 },
 "techer2" : {
 "name" : "ABC",
 "year" : 2001
 },
 "techer3" : {
 "name" : "RST",
 "year" : 2015
 }
}
sem1_student = {
 "student1" : {
 "name" : "UVW",
 "year" : 2024
 },
 "student2" : {
 "name" : "JKL",
 "year" : 2022
 },
 "student3" : {
 "name" : "MNO",
 "year" : 2025
 }
}
#Year Code goes here
print("All Sem")
print(sem.sem1_techers)
print(sem.sem1_student)
#Engineering code goes here
sys.path.insert(0, './engineering') #setting packages path
#import engineering.years as enggimport sem
import sys
print("From Enginggring")
print(years.sem.sem1_techers)
print(years.sem.sem1_student)
