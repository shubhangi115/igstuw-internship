# file: a storage space where you can save data on permananent basis
# how data can be persisted in python? ----> file handling 
# types ----->> .csv(comma delimited file), .xls or .xlsx file(excel), .jason(object file)
# .csv files
# 2 ways of working with csv files:
# 1. csv module
# 2. pandas module

# csv module

# import csv 
# to create a simple file anf use it for writing 
# a file can have in general 2 modes -> "w" for writing and "r" mode fpr reading

# with open("firstfile.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["empid","empname","salary","department"])
#     writer.writerow([101,"Ajay",1000000000,"marketing"])
#     writer.writerow([102,"Reema", 2000000000,"production"])
#     writer.writerow([103,"Reema", 3000000000,"production"])

# write with loop

import csv
data_list=[
    ["empid","empname","salary","department"],
    [101,"Ajay",1000000000,"marketing"],
    [102,"Reema", 2000000000,"production"],
    [103,"Reema", 3000000000,"production"],
]
with open('secondfile.cs', 'w', newline='') as file:
    writer = csv.writer (file,delimiter='|')
    writer.writerows(data_list)
