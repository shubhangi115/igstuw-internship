# NUMERIC DATA TYPES
# num1=10
# print("the num is : ", num1, "the type is: ", type(num1))
# num1=10.12
# print("the num is : ", num1, "the tyoe is: ", type(num1))
# num1=10+5j #complex numbers
# print("the num is : ", num1, "the tyoe is: ", type(num1))

#NUMBER SYSTEMS
#INTEGER BASE 10
#BINARY BASE 2 FOR USING BINARY NUMBERS -->>PREFIX 0B OR 0b
#octal -->> 0o or 0B
#hexadecimal -->> 0x or 0X

# Floating point numbers -> python default data type is float
# complex number

# print(0b101)
# print(0o156)
# print(oxAFB) # 0 to 9 10-A,11-B.....15-F

#TYPE CASTING IN NUMBER IS AUTOMATIC OR IMPLICIT
#AT TIME WE MAY NEED TO FORCE TYPECASTING SO THERE IT WILL BE EXPLICIT
# EXPLICIT --> CONVERT BIG DATA TYPE INTO SMALL

# num1= int(15.77)
# print(num1)
# val= int(-55.88)
# print(val)
# val1=complex("10+5j")
# print(val1)
# print(type(val1))

# NUMBER BASED MODULE -> RANDOM AND MATH MODULE
#RANDOM MODULE --> GENERATE NUMBERS RANDOMLY ON THE FLY

#RANDOM MODULE
# import random
# print(random.randrange(20,50)) #generate number from (20,50)
# print(random.random()) #generate random number

# #we can also pick a value randomly from any sequence

# list1=["hello","hi","holla","bonjour"]
# print(random.choice(list1))
# random.shuffle(list1)
# print(list1)

#MATH MODULE

#mathmatical calculation

# Aliases means nick names
# import math as mt #mt as alias name for math
# print(mt.factorial(5))
# print(mt.pi)
# print(mt.log10(10000000)) 
# print(mt.pow(2,3))  #2^3=2*2*2

# SEQUENCE DATA -->> LIST, TUPLE AND STRING

#LIST----->> MOST FLEXIBLE SEQUENCE OF DATA AS T ALLOWS ALL SORT OF MODIFICATION
#[] BRACKETS CREATE LIST
# DATA IN LIST CAN BE OF DIFFERENT DATA TYPES
# INDEX STARTS -->0, -1 FROM LAST
#ORDERED BY POSITION, MUTABLE , REPEATED OR DUPLICATE VALUES ARE ALLOWED

# list=[1,2,3,"hello","bye",12.77,"true","false"]
# print(list[0])

# TUPLE -->> SEQUENCE OF DATA HABVING ORDER OF ELEMENTS BUT ARE IMMUTABLE
#() -->> ARE USED
# INDEX STARTS -->0 , -1 FROM LAST
#IT MAY CONTAIN ANY TYPE OF DATA

# tup1=(1,2,3,"hello",True, 12.66)
# print(tup1[2])
# print(tup1[3][1])

#immutability
# list1=[1,2,3,"hello","bye",122.77,True,False,"Go"]
# tup1=(1,2,3,"hello","bye",122.77)
#try to modify last element of list from "Go" to "Gonow"
# print("original list: ",list1)
# list1[-1]="Gonow"
# print(list1)
#list are mutable

# tup1[-1]=100
# print(tup1)
# immutability of tuple

# dictionary 
# set
# these are the data types that do not have any index or positions

# create a dictionary 
# mutable-----> only values
# braces brackets
# values are in form of key:value pairs
# each value is recognised by key
# keys should be different as they are differentiater and values can be same

# dict={"Name":"Ajay","Age":20, "Salary":10000, "House":20}
# print(dict["Age"])
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# dict["Age"]=25
# print(dict)
# dict["degree"]="B.tech"
# print(dict)

# sets 
# used with {}
# No duplicates elements allowed
# on printing the order may change
set={1,2,3,3,4,5,6,6,6,7,8,8,9,9,9,9,9,}
print(set)
