# import keyword
# #keyword module is used to see all keywords in python
# print(keyword.kwlist)
# print(len(keyword.kwlist)) #calculate the lenght of keyword list

#INPUT THEN TYPE OF DATA TYPE SYNTAX
#OOPS--->>> every type in python is an object of a class
#TYPE CASTING ---> int(),str(),float()

#demo for print command
# print(7,9,8,10, sep='%', end='$$')
#sample file here is a file object for writing

# samplefile=open(r'C:\Users\i5\OneDrive\Desktop\demo file\demo.txt','w')

#  there are two modes to open a file - "r " for reading and "w " for writing "a" for append
# print(7,9,8,10, sep='%', end='$$', file =samplefile)

# output formatting sor string
# print("hello all {} people in class".format("10"))

#IDENTIFIERS AND CONCATENATION
# I="10"     #for string "+" is used to concatenation
# J="90"
# K=I+J
# print(K)

# I=10 
# J=90
# K=I+J
# print(K)

# FOR ADDING a string and int/float we use type casting.......
#we will type caste int/float into string as string can't be converted to int/float, also string is generic datatype
#OVERLOADED OPERATORS

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
set={1,2,3,3,4,5,6,6,6,7,8,8,9,9,9,9,9,}
print(set)

# H=len([1, 2, 3])
# print(H)
# str = "hello" \
#       "hello" \
#       "meow"
# print(str)
# slicing syntax
#  str[starting_index_pos:stop_index_pos:No. of moves or jump]
#"Hello all"
#str[1:5]


# str1 = "Hello all"
# # Negative slicing
# print(str1[-5:-1])
# print(str1[-1:-5])
# print(str1[-7::2])
# print(str1[::-1])




#String Comparison

#>,<,== -> to check for equality
# str1 = "Hello"
# str2 = "hello"
# print(str1 == str2)
# print(str1>str2)
# print(str1> str2)

#Ascii codes
#A-Z = 65 to 90
#a-z =97-122
#ord() -> gives ascii value of char
#chr() -> gives corresponding chars for a given ascii code
# print(ord("H"))
# print(ord("h"))
# print(chr(65))
# (print(chr(97)))

#String repeatition
 #* operator to reapeat string multiple times

# str1 = "Hello"
# print(str1*2) 
# print(str1*5)

# #concatenation operator
# str1 = "Hello"
# str2 = " "
# str3 = "All"
# print(str1+str2+str3)

# #Find length or number 
# str1 ="Hello all"
# print("The no. of characters in string are :",len(str1))

# list 
#creating list
# list1=[1,2,3,4,"abc",True,11.89,4+5j]
# print("the list is: ", list1)

# #how to create a blank list
# list2=[] #empty list
# print(list2)

#since python is object oriented it has everything in form of object
#list here in pyhton is also a class. a list object can be also instantiate by list class
#construcyor by invoking list()

# str1= "hello All"
# # to convert this directly to list we can invoke list()
# new_list=list(str1)
# print("the newley formed list is: ",new_list)

#properties of list:
""" 1. ordered 
    2. mutable
    3. allows repeated values i.e. duplicates"""

# 1. ordered --->> each element of list has an index position atteched

# list1=[1,2,3,"hello",11.4,4+5j]
#start access from left to right
# print("first ", list1[0])
# print("first ", list1[1])
# print("first ", list1[2])
# print("first ", list1[3])
# print("first ", list1[4])
# print("first ", list1[5])

#slice and water negative-slice a list
# list1= [1,2,3,"hello",11.4,4+5j]
# #slice list from index 1 to 6
# print("slice from index 1 to 6 ", list1[1:6])
# print("negative slice from last position to second element ", list1[1:-1])
# print(len(list1))
# print(len(list1)/2)

#2 Mutable : You an modify elements, add and remove elements from list

# list1=[1,2,3,"abc",11.5,4+5j]
# print("original list; ", list1)
# append() ---->> to add a new element at the end of the list 
# list1.append("new value")
# print(" the appended list: ",list1)

# insert ----->> to add element to a specific position
# list1=[1,2,3,"abc",11.5,4+5j]
# print("original: ",list1)
# list1.insert(3,20) # insert(index, value to be inserted)
# print("updated list: ", list1)

# extend() ----->> you can add new values form another list into original list
# list1=[1,2,3,"abc",11.5,4+5j]
# print("original: ",list1)
# list2=[7,8,9,"go"]
# list1.extend(list2)
# print("updated list", list1)
# print("list 2 values: ", list2)

#list concatenate
# list1=[1,2,3,"abc",11.5,4+5j]
# list2=[7,8,9,"go"]
# print("list concatenation: ",list1+list2)

# 3. list repetation
# print("list repeate: ", list1*3)

#operators common for sequence: +,*,[:]

# make modification in list
# list1=[1,2,3,"abc",11.5,4+5j]
# print("original list: ",list1)
#update the third element of list 3 --->> 30
# list1[2]= 30
# print("updated: ", list1)
# list1[2:5]=[30,"hello", "byee",11] # no error when elements are added more than the index number
# print("updated list: ",list1)

# remove() ---->>> Remove elements from list
# list1=[1,2,3,"abc",11.5,4+5j,"abc"]
# print("original list: ",list1)

# list1.remove("abc")
# print("updated list: ",list1)
# list1.remove("abc")
# print("updated list: ",list1)

# count() ---->> count occurence of elemets
# list1=[1,2,3,"abc",11.5,4+5j,"abc"]
# print("original list: ",list1)
# print("count 'abc': ",list1.count("abc"))

#sort a list
# print("the sorted : ",list1.sort())
#sorting works with same dataypes

# list1=[1,2,4,1,3,2,9,0,880]
# list1.sort() #in ascending
# print("the sorted : ",list1)

#sort in descending or reverse 
# list1.sort(reverse=True)
# print("the sorted : ",list1)
# #for string also
 # copy() ---->> create a copy of list 
# list1=[1,2,4,1,3,2,9,0,880]
# print("original list: ",list1)
# newlist=list1.copy()
# print("new list: ",newlist)

#to check list is same or not
#print(list1==newlist)

# TUPLE -----> it is a sequence like list with some differences
# 1. list is mutable but tuple is immutable
# 2. list starts with [] while tuple starts with ()
# 3. there is a fairly good number of methods in list while only 2 methods for tuple

# creating a tuple
# tup1=(1,2,3,4,"hello",11.44, True,False,3+3j)
# print("the original tuple: ",tup1)
# we have a tuple constructor tuple()
# newtup=tuple(("hello","bye",1,2,3,22.44))
# print("new tuple ", newtup)
# list1=["hello","bye",1,2,3,22.44]
# newtup=tuple(list1)
# print("new tuple ", newtup)
# tup1=(1,2,3,"hello",True,1,2,3)
# list1=list(tup1)
# print("list from tuple: ",list1)
# str1="hello"
# newtup=tuple(str1)
# print("tuple from string: ",newtup)

# empty or blank tuple
# tup1=()
# print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

# create a tuple with only single value
# tup1=("hello")   # interpreter will consider this tuple as string as it is a single value tuple and without a comma it will consider a string......but using comma after that it will generate tuple
# print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))
# tup1=(25)
# print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))
# tup1=("hello",)
# print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))
# tup1=(25,)
# print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))
# singleton tuple ---->> single value tuple(need to put comma after value)
# list=[22] # n need to add comma in list
# print("the list ",list,"type of list ", type(list))

#default datatype of python is tuple
# val=1,2,3,5,"go"
# print("the values are ",val,"type of list ", type(val))

# properties for tuples
""" 1. ordered
    2. immutable
    3. allows duplicate values"""

# 1.orrdered
# tup1=(1,2,3,4,"hello",11.44, True,False,3+3j)
# print("the original tuple: ",tup1)
# print("the first element: ", tup1[0])
# print("the first element: ", tup1[1])
# print("the first element: ", tup1[2])
# print("the first element: ", tup1[3])
# slicing just like list

# 2. immutable
# list1=[1,2,3,"hello",11.55]
# print("original list: ",list1)
# tup1=(1,2,3,"hello",11.55)
# print("original tup1: ",tup1)
#try to modify 3---->>> in both list1 and tup1
# list1[2]=30 
# tup1[2]=30  # immutability
# print("updated list: ",list1)
# print("updated tuple: ",tup1)
# security stored data are used in tuple(you dont want data to be changed even unintentionally)

# to find the number or count of lements in tuple
# len()
# tup1=(1,2,3,"hello",11.55)
# print("original tup1: ",tup1)
# print("lenght ", len(tup1))

#check for membership in tuple 
#check if "hello" exists in tuple
# print('hello in tuple ',"hello" in tup1)
# print('Hello in tuple ',"Hello" in tup1)
# print('hello in tuple ',"hello" not in tup1)

# no direct removal of elements allowed in tuple
# however you can remove tuple in one go
# del property
# del tup1
# print(tup1)  #this line will show error as tup 1 is removed in line 372

# Two method in tuple;
# 1. count(): count the number of occurence number of times
# 2. index(): search and find index of an elemnt otherwise throw exeption
# tup1=(1,2,3,"hello",11.55,"hello","Hello")
# print("original tup1: ",tup1)
# print("count of hello: ",tup1.count("hello"))
# print("find if 'hello' is present: ", tup1.index("hello"))  # searches for first occurence index only

# Set
# properties
# set begin with {} braces
# it does not allow duplicates
# constructor call set()
# unordered
# no slicing and indexing

# creating set()
# set1={1,2,3,True,11.55,"hello",4+6j,1,1,1,2,2}  
# print("set: ",set1)

#empty set
# set2=set()
# print("the empty set is: ",set2,"type of set: ",type(set2))
# set3={}  # this is dictionary as dictionary also include {}
# print("the empty set is: ",set2,"type of set: ",type(set3))

# set is mutable
# add() ---->> to add new element
# set1={1,2,3,4,5,6,7,8}
# print("original: ",set1)
# set1.add(55)
# print("updated: ",set1)
# set1.add(100)
# print("updated: ",set1)
# set1.add(515)
# print("updated: ",set1)

# update() --->> to add elements from another list of tuple in a set

# set1={1,2,3,4,5,6,7,8}
# print("original: ",set1)
# list1=[11,12,13,14,15]
# set1.update(list1)
# print("updated set: ",set1)
# tup1=(1,2,3,4,100)
# set1.update(tup1)
# print("updated set: ",set1)
# set2={1000,1003}
# set1.update(set2)
# print("updated: ",set1)

# remove values from set
# set1={1,2,3,4,5,6,7,8}
# print("original: ",set1)
# remove() ----->> removes particular value from set and throw error if value not found or when value is removed once
# set1.remove(5)    # if you give repeated value in set python will not consider repeated value
# print("updated: ",set1)
# set1.discard(5)   # whereas discard will not throw error even value is removed once
# print("updated: ",set1)
# set1.discard(5)
# print("updated: ",set1)

# set2={True,False,1,"Hello"}
# print(set2) 
"""Ma'am this command returns True instead of 1
It give output {False, True, 'Hello'}

since set is specifically unpredictable only when value is boolean or 0,1"""

# set is used in mathematical operations.......union,intersection,difference

# builtin methods of sets
# all() --->> checks for the true set of boolean values
# this method is also applicable for list and tuple
# set1={True,True,True}   # 1---->true   0--->false
# res=all(set1)
# print("result is: ",res)

# any() -----> returns true if atleat 1 value in an iterable is true
# set1={True,True,False}
# res=any(set1)
# print("result is: ",res)

# len() --->length of set
# set1={1,2,3,4,"hello",11.45}   
# res=len(set1)
# print("result is: ",res)

# set2={True,True,False,1,1,0,0}   # since sets considers dupliacte values as 1 and it will take 1 and true as same
# res=len(set1)
# print("result is: ",res)

# max() and min()
# generic function it is used in any data type
# set1={1,2,4,5,6,7,-11,-22}
# res=min(set1)
# print("min: ",res)

# set1={1,2,4,5,6,7,-11,-22}
# res=max(set1)
# print("max ",res)

# sum() ----> adding elements,,,,for all datatypes
# set1={1,2,4,5,6,7}
# res=sum(set1)
# print("the sum result is: ",res)

# mathematical set operations
# union,intersection,symetric difference, subtraction
# union --->> cobines unique elements from set A and B
# union() and | operator -->> pip operator
# set1={1,2,3,4,5}
# set2={5,6,7,8,9}
# print("using union(): ", set1.union(set2))
# print("using |: ", set1 |set2)

# intersection : takes common elements
# intersection () and & operator
# set1={1,2,3,4,5}
# set2={5,6,7,8,9}
# print("using intersection(): ", set1.intersection(set2))
# print("using &: ", set1&set2)

#difference() ----> A-B ---> subtracts common element
# difference() and - operator
# set1={1,2,3,4,5,6}
# set2={5,6,7,8,9}
# print("using difference(): ", set1.difference(set2))
# print("using -: ", set1-set2)
# print("original set1 ",set1)
# print("original set2 ",set2)
# in-place ---- if original memory of set are changed
# --->> intersection_update(), union_update(), difference_update()
# out of place ---- at temporary location

#in-place 

# set1={1,2,3,4,5,6}
# set2={5,6,7,8,9}
# print("original set1 ",set1)
# print("original set2 ",set2)
# set1.intersection_update(set2)
# print("the updated set1: ", set1)
# print("the updated set2: ", set2)

# difference update
# set1={1,2,3,4,5,6}
# set2={5,6,7,8,9}
# print("original set1 ",set1)
# print("original set2 ",set2)
# set1.difference_update(set2)
# print("the updated set1: ", set1)
# print("the updated set2: ", set2)

# update().......for combining two sets like union

# symmetric diffrence ----->> returns all the values present in given set data structure except common values
# set1={1,2,3,4,5,6}
# set2={5,6,7,8,9}
# print("original set1 ",set1)
# print("original set2 ",set2)
# print("the result of symmetric difference: ",set1.symmetric_difference(set2))
# print("the updated set1: ", set1)
# print("the updated set2: ", set2)

# symmetric_difference_update---->> in-place
# set1={1,2,3,4,5,6}
# set2={5,6,7,8,9}
# print("original set1 ",set1)
# print("original set2 ",set2)
# print("the result of symmetric difference update: ",set1.symmetric_difference_update(set2))
# print("the updated set1: ", set1)
# print("the updated set2: ", set2)





# AI-ML