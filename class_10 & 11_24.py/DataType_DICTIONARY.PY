"""
DICTIONARY
it contain element in format of key:value pair
properties:
    starts with {}
    mutable
    unordered
    no indexing 
    empty dictionary speacified by {} and set by set()

empty dict
dict1={}
print("the dict1 value: ",dict1, "the type is : ", type(dict1))
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}    #values can be same but not key
print("the dict values are: ",dict1)

*Access elements in dict with help of keys

dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20} 
print("the emp name: ",dict1["Ename])

1. unordered ---> both set and dictionary are collection type so, they are unordered

2. mutable
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20} 
dict1["Degree"]=["BCA",'MCA']
print("the dict1 is: ",dict1)
print("the degrees are: ",dict1['Degree'])

3. to update the existing value 
change age from 20 to 22
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
dict1["age"]=22
print("the updated dict1 is: ",dict1) 

4. REMOVE
use del property

dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
del dict1["salary"]
print("the updated dict1 is: ",dict1) 

pop() 
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
res=dict1.pop("salary")
print("the updated dict1 is: ",dict1) 
print("the popped value: ",res) 

5. LENGTH
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
print("the lenght of dict1 is: ",len(dict1))

6. TO ACCESS KEYS
keys()
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
print("keys are: ",dict1.keys())

7. TO ACCESS VALUES
values()
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
print("values are: ", dict1.values())

8. TO ACCESS ITEMS --->> will give list of multiple tuples of key value pairs
items()
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
print("the items are: ",dict1.items())

9. GET ----> TO GET A VALUE OF CORRESPONDING TO A KEY
dict1={"Ename":"ajay","age":20,"salary":1000000,"houseNo":20}
print("the value of house no. is: ",dict1.get("houseNo"))

"""


