"""
Set
properties
    set begin with {} braces
    it does not allow duplicates
    unordered
    no slicing and indexing

creating set()
constructor call set()

set1={1,2,3,True,11.55,"hello",4+6j,1,1,1,2,2}  
print("set: ",set1)

empty set
set2=set()
print("the empty set is: ",set2,"type of set: ",type(set2))
set3={}  # this is dictionary as dictionary also include {}
print("the empty set is: ",set2,"type of set: ",type(set3))

1. set is mutable
add() ---->> to add new element

set1={1,2,3,4,5,6,7,8}
print("original: ",set1)
set1.add(55)
print("updated: ",set1)

set1.add(100)
print("updated: ",set1)

set1.add(515)
print("updated: ",set1)

2. UPDATE -->> update() --->> to add elements from another list of tuple in a set

set1={1,2,3,4,5,6,7,8}
print("original: ",set1)

list1=[11,12,13,14,15]
set1.update(list1)
print("updated set: ",set1)

tup1=(1,2,3,4,100)
set1.update(tup1)
print("updated set: ",set1)

set2={1000,1003}
set1.update(set2)
print("updated: ",set1)

3. REMOVE --> remove values from set
* remove() ----->> removes particular value from set and throw error if value not found or when value is removed once
keyerror exception 
set1={1,2,3,4,5,6,7,8}
print("original: ",set1)

set1.remove(5)    # if you give repeated value in set python will not consider repeated value
print("updated: ",set1)

* dicard() simply does nothing if the value for deletion is not found
set1.discard(5)   # whereas discard will not throw error even value is removed once
print("updated: ",set1)

set1.discard(5)
print("updated: ",set1)

set2={True,False,1,"Hello"}
print(set2) 

Ma'am this command returns True instead of 1
It give output {False, True, 'Hello'}
since set is specifically unpredictable only when value is boolean or 0,1


set is used in mathematical operations.......union,intersection,difference

4. builtin methods of sets
(A) all() --->> checks for the true set of boolean values....this method is also applicable for list and tuple
set1={True,True,True}   # 1---->true   0--->false
res=all(set1)
print("result is: ",res)

(B) any() -----> returns true if atleat 1 value in an iterable is true
set1={True,True,False}
res=any(set1)
print("result is: ",res)

(C) len() --->length of set
set1={1,2,3,4,"hello",11.45}   
res=len(set1)
print("result is: ",res)

set2={True,True,False,6,1,1,0,0}   # since sets considers dupliacte values as 1 and it will take 1 and true as same
res=len(set2)
print("result is: ",res)

(D) max() and min()
generic function--->it is used in any data type
set1={1,2,4,5,6,7,-11,-22}
res=min(set1)
print("min: ",res)

set1={1,2,4,5,6,7,-11,-22}
res=max(set1)
print("max ",res)

(E) sum() ----> adding elements,,,,for all datatypes
set1={1,2,4,5,6,7}
res=sum(set1)
print("the sum result is: ",res)

5. mathematical set operation ---> union,intersection,symetric difference, subtraction

(A) union --->> cobines unique elements from set A and B
union() and | operator -->> pipe operator

set1={1,2,3,4,5}
set2={5,6,7,8,9}
print("using union(): ", set1.union(set2))
print("using |: ", set1 |set2)

(B) intersection : takes common elements
intersection () and & operator

set1={1,2,3,4,5}
set2={5,6,7,8,9}
print("using intersection(): ", set1.intersection(set2))
print("using &: ", set1&set2)

(C) difference() ----> A-B ---> subtracts common element
difference() and - operator

set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print("using difference(): ", set1.difference(set2))
print("using -: ", set1-set2)
print("original set1 ",set1)
print("original set2 ",set2)

in-place ---- if original memory of set are changed
--->> intersection_update(), union_update(), difference_update()
out of place ---- at temporary location

in-place operation
(D) Intersection_update()
set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print("original set1 ",set1)
print("original set2 ",set2)
set1.intersection_update(set2)
print("the updated set1: ", set1)
print("the updated set2: ", set2)

(E) difference update
set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print("original set1 ",set1)
print("original set2 ",set2)
set1.difference_update(set2)
print("the updated set1: ", set1)
print("the updated set2: ", set2)

for union update we have -- >> 
update().......for combining two sets like union

(F) symmetric diffrence ----->> returns all the values present in given set data structure except common values
IT IS out of place

set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print("original set1 ",set1)
print("original set2 ",set2)
print("the result of symmetric difference: ",set1.symmetric_difference(set2))
print("the updated set1: ", set1)
print("the updated set2: ", set2)

(G) symmetric_difference_update---->> in-place
set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print("original set1 ",set1)
print("original set2 ",set2)
print("the result of symmetric difference update: ",set1.symmetric_difference_update(set2))
print("the updated set1: ", set1)
print("the updated set2: ", set2)

(H) isssuperset(), issubset(), isdisjoint()
set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9,10}
print("if set 1 is a subset of set 2 :", set1.issubset(set2))
print("if set 1 is a superset of set 2 :", set1.issuperset(set2))
print("if set 2 is a subset of set 1 :", set2.issubset(set1))
print("if set 2 is a superset of set 1 :", set2.issuperset(set1))
print("if set 1 and set 2 are disjoint or not :", set1.isdisjoint(set2)) 

(I) pop(): it randomly delete value from set
set1={1,2,3,4,5,6,7,8,9,10}
print("The removed value is: ",set1.pop())
print("the original set: ",set1)

# error will be given when there is only one value in set and pop method is used twice
set1={10}
print("The removed value is: ",set1.pop())
print("the original set: ",set1)
print("The removed value is: ",set1.pop())

set1={20,25}
print("The removed value is: ",set1.pop())
print("the original set: ",set1)
print("The removed value is: ",set1.pop())

"""



