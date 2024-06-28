
"""
list 
creating list

list1=[1,2,3,4,"abc",True,11.89,4+5j]
print("the list is: ", list1)

how to create a blank list
list2=[] #empty list
print(list2)

since python is object oriented it has everything in form of object
list here in pyhton is also a class. a list object can be also instantiate by list class constructor by invoking list()

str1= "hello All"   # to convert this directly to list we can invoke list()
new_list=list(str1)
print("the newley formed list is: ",new_list)

properties of list:
    1. ordered 
    2. mutable
    3. allows repeated values i.e. duplicates

1. ordered --->> each element of list has an index position atteched

list1=[1,2,3,"hello",11.4,4+5j]
start access from left to right
print("first ", list1[0])
print("first ", list1[1])
print("first ", list1[2])
print("first ", list1[3])
print("first ", list1[4])
print("first ", list1[5])

* slice negative-slice a list

list1= [1,2,3,"hello",11.4,4+5j]
#slice list from index 1 to 6
print("slice from index 1 to 6 ", list1[1:6])
print("negative slice from last position to second element ", list1[1:-1])
print(len(list1))
print(len(list1)/2)

2 Mutable : You can modify elements, add and remove elements from list

list1=[1,2,3,"abc",11.5,4+5j]
print("original list; ", list1)

(A) append() ---->> to add a new element at the end of the list 
list1.append("new value")
print(" the appended list: ",list1)

(B) insert ----->> to add element to a specific position
list1=[1,2,3,"abc",11.5,4+5j]
print("original: ",list1)
list1.insert(3,20) # insert(index, value to be inserted)
print("updated list: ", list1)

(C) extend() ----->> you can add new values form another list into original list
list1=[1,2,3,"abc",11.5,4+5j]
print("original: ",list1)
list2=[7,8,9,"go"]
list1.extend(list2)
print("updated list", list1)
print("list 2 values: ", list2)

3. CONACATINATION
list1=[1,2,3,"abc",11.5,4+5j]
list2=[7,8,9,"go"]
print("list concatenation: ",list1+list2)

4. list repetation
print("list repeate: ", list1*3)

operators common for sequence: +,*,[:]

5. make modification in list
list1=[1,2,3,"abc",11.5,4+5j]
print("original list: ",list1)

update the third element of list 3 --->> 30

list1[2]= 30
print("updated: ", list1)
list1[2:5]=[30,"hello", "byee",11] # no error when elements are added more than the index number
print("updated list: ",list1)

6. remove() ---->>> Remove elements from list

list1=[1,2,3,"abc",11.5,4+5j,"abc"]
print("original list: ",list1)
list1.remove("abc")
print("updated list: ",list1)
list1.remove("abc")
print("updated list: ",list1)

7. count() ---->> count occurence of elemets
list1=[1,2,3,"abc",11.5,4+5j,"abc"]
print("original list: ",list1)
print("count 'abc': ",list1.count("abc"))

8. sort a list --> sorting works with same dataypes

list1=[1,2,4,1,3,2,9,0,880]
print("the sorted : ",list1.sort())
list1.sort()      #in ascending
print("the sorted : ",list1)

* sort in descending or reverse 

list1.sort(reverse=True)
print("the sorted : ",list1)
#for string also

9. copy() ---->> create a copy of list 

list1=[1,2,4,1,3,2,9,0,880]
print("original list: ",list1)
newlist=list1.copy()
print("new list: ",newlist)

10. to check list is same or not
print(list1==newlist)
"""