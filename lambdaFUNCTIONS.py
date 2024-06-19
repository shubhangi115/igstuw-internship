#lambda function
# anonymous function- user defined function codes that do not have a name
#you don't have to use def keyword to create lambada function
# syntax:
# variable=lambda argument(s): expression statements or calculations
# to call lambda function 
# variable()

# use lambda function for printing a message
# message=lambda:print("hello")
# calling a lambda function
# message()

# use arguments in lambda function
# message=lambda username:print(f"hello user {username}!!")
# calling a lambda function
# username=input("enter your username: ")
# message(username)

# it is used for single liner code we use lambda function


# Join lambda functions with map() and filter() methods

# from a list of numbers we want to filter out only odd numbers and create a new list from it

# syntax:

# filter(any function to be used as filter ex. lambda,iterable )
# list1=[1,2,3,4,5,6,7,8,9,10]
# odd_list= list(filter(lambda num:(num%2!=0),list1))
# print("The new odd list is: ",odd_list)

# even_list=list(filter(lambda num: (num%2==0),list1))
# print("the even list: ",even_list)

# RESULT of max b/w two numbers
# result=lambda num1,num2: num1 if (num1>num2) else num2

# num1=int(input("enter num1 "))
# num2=int(input("enter num2 "))
# ans =result(num1,num2)
# print("the max is:",ans)

# check for age60 list and filter out those employees in a seperate list
# ages_list=[23,56,67,88,90]
# senoir_age=list(filter(lambda ageval:ageval>=60, ages_list))
# print("the seperate senoir list: ", senoir_age)

# map() ----> helps to apply a lambda function calculation mapped to each element of iterables
# map(lambda.., iterable)
# list_salary=[1000,20000,2000000000,4500000000000]
# add bonus of 500 rs to all salaries and create a bonus list

# bonus_list = list(map(lambda sal:sal+500, list_salary))
# print(bonus_list)

# covert every employee name to be converted to uper case 
# list_emp=["ajay","ritu","SEEMA", "Raman","ReeMA"]
# proc_list_emp=list(map(lambda emp: emp.upper(),list_emp))
# print(proc_list_emp)

