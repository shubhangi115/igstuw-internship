"""
* LOOPS

1. for loop: it should be used if the number of repitions or iteration are known in advance
syntax:
    for iterative_variable in sequence:
        code_statement(s)
USING: 

list1=[1,2,3,4,5,"hello"]
for i in list1:
    print("the value of list is: ",i)

* RANGE---->> range()--> it generates numbers in a given range
syntax: range(start,stop,steps)  starts is by deafult if not given, stop is mandatory to give and print stop-1

values = range(10)  # 0 to 9
for i in values:
    print("The generated value is: ",i)


values = range(5,51)  
list1=list(values)
for i in values:
    print("The generated value is: ",i)
print("The list is: ",list1) 

values = range(-5,4)  
list1=list(values)
for i in values:
    print("The generated value is: ",i)
print("The list is: ",list1) 

values = range(1,11,2)  
list1=list(values)
for i in values:
    print("The generated value is: ",i)
print("The list is: ",list1)

values = range(5,-6,-1)   # will print in reverse order  
list1=list(values)
for i in values:
    print("The generated value is: ",i)
print("The list is: ",list1)

values = range(5,-6,1)   # will give blank list
list1=list(values)
for i in values:
    print("The generated value is: ",i)
print("The list is: ",list1)  

list1=["ajay","shubhangi","shivangi","aditya"]
count=0
for i in list1:
    print("name of employee: ",i)
    count=count+1
else:
    print("total number of employee: ",count) 
   
**** list1=[1,2,3,4]
for _ in list1:    
    print("LOOP WORKING TEST SUCCESS") 
    
* NESTED LOOP

for i in range(5):
    for j in range(4):
        print("i: ",i,"j: ",j)


2. while loop: it should be used when number of iterations are not known in advance
syntax:
    while conditional_expression:
        code_statement(s)

EXAMPLES
if the user has entered correct password for login. else the user is asked to retry again
the scenerio says the user can try infinite times

QUES1. Again again and again till user enter correct password answer
while True:
    passw=input("enter yor password:")
    if passw=="password":
        print("you are welcome")
        break
    else:
        pass    # for again again and again till user enter correct answer
        # or can print anything 

QUES2. Calculate the sum of numbers till user enter "QUIT"

num=int(input("enter number "))
choice=input("you want to continur or quit ")
sum=num
while True:
    if choice.upper()=="QUIT":
        break
    elif choice.upper()=="YES" or choice.upper()=="Y" :
        num2=int(input("enter next number "))
        sum=sum+num2
        print("the sum is: ",sum)
        choice=input("you want to continur or quit ")
    else:
        print("enter relevent choice ullu ")
        choice=input("you want to continur or quit ")
    
* BREAK,CONTINUE,PASS

for i in range(10): 
    if i==7:
        print("Limit to 7 reached!!")
        break
    else:
        print("The value is: ", i)
else:
    print("The Loop ended at 7!!")"""

list1= ['Ajay', 'Raman', 'Mona', 'Priya', 'Manan'] 
salary =1000
# Want no appraisal for Priya
for i in list1: 
    if i=="Priya":
        continue
    elif i=="Ajay" or i=="Manan": 
        print("User!!: ", i)
    else:
        pass

