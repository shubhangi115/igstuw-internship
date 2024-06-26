"""TUPLE -----> it is a sequence like list with some differences
1. list is mutable but tuple is immutable
2. list starts with [] while tuple starts with ()
3. there is a fairly good number of methods in list while only 2 methods for tuple

creating a tuple

tup1=(1,2,3,4,"hello",11.44, True,False,3+3j)
print("the original tuple: ",tup1)

we have a tuple constructor tuple()

newtup=tuple(("hello","bye",1,2,3,22.44))
print("new tuple ", newtup)

list1=["hello","bye",1,2,3,22.44]
newtup=tuple(list1)
print("new tuple ", newtup)

tup1=(1,2,3,"hello",True,1,2,3)
list1=list(tup1)
print("list from tuple: ",list1)

str1="hello"
newtup=tuple(str1)
print("tuple from string: ",newtup)

empty or blank tuple
tup1=()
print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

create a tuple with only single value

tup1=("hello")   # interpreter will consider this tuple as string as it is a single value tuple and without a comma it will consider a string......but using comma after that it will generate tuple
print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

tup1=(25)
print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

tup1=("hello",)
print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

tup1=(25,)
print("the tup1 is : ", tup1,"type of tup1 ", type(tup1))

singleton tuple ---->> single value tuple(need to put comma after value)

list=[22] # n0 need to add comma in list
print("the list ",list,"type of list ", type(list))

#default datatype of python is tuple
# val=1,2,3,5,"go"
# print("the values are ",val,"type of list ", type(val))

# properties for tuples
    1. ordered
    2. immutable
    3. allows duplicate values

1.orrdered
tup1=(1,2,3,4,"hello",11.44, True,False,3+3j)
print("the original tuple: ",tup1)
print("the first element: ", tup1[0])
print("the first element: ", tup1[1])
print("the first element: ", tup1[2])
print("the first element: ", tup1[3])
slicing just like list

2. immutable
list1=[1,2,3,"hello",11.55]
print("original list: ",list1)

tup1=(1,2,3,"hello",11.55)
print("original tup1: ",tup1)

try to modify 3---->>> in both list1 and tup1
list1[2]=30 
tup1[2]=30  # immutability
print("updated list: ",list1)
print("updated tuple: ",tup1)

security stored data are used in tuple(you dont want data to be changed even unintentionally)

OPERATION

1. LENGTH --> to find the number or count of elments in tuple
* len()

tup1=(1,2,3,"hello",11.55)
print("original tup1: ",tup1)
print("lenght ", len(tup1))

2. MEMBERSHIP ---> check for membership in tuple 
check if "hello" exists in tuple
print('hello in tuple ',"hello" in tup1)
print('Hello in tuple ',"Hello" in tup1)
print('hello in tuple ',"hello" not in tup1)

3. REMOVAL ---> no direct removal of elements allowed in tuple....however you can remove tuple in one go
* del property
  del tup1
print(tup1)  #this line will show error as tup 1 is removed in line 101

4.
Two method in tuple;
1. count(): count the number of occurence number of times
2. index(): search and find index of an elemnt otherwise throw exeption
tup1=(1,2,3,"hello",11.55,"hello","Hello")
print("original tup1: ",tup1)
print("count of hello: ",tup1.count("hello"))
print("find if 'hello' is present: ", tup1.index("hello"))  # searches for first occurence index only

"""