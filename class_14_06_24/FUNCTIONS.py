"""
FUNCTIONS
-> FUNCTIONS ARE USED TO GROUP TOGETHER A CERTAIN NUMBER OF RELATED INSTRUCTIONS
-> THESE ARE REUSABLE BLOCKS OF CODES WRITTEN TO CARRY OUT A SPECIFIC TASK
-> IT MIGHT OR MIGHT NOT REQUIRE INPUTS
-> THEY ARE ONLY EXECUTED WHEN THEY ARE SPECIFICALLY CALLED
-> DEPENDING ON THE TASK A FUNCTION IS SUPPOSED TO CARRY OUT , IT MIGHT NOT RETURN VALUE
-> THERE ARE THREE TYPES OF FUNCTION:
    1. PRE-DEFINED/BUILT-IN
    2. USER-DEFINED
    3. LAMBDA

1. PRE-DEFINED FUNCTION
Eg: abs()
    bin()
    len()
    list()
    max()
    min()
    range()
    int()
    input()....
2. USER-DEFINED FUNCTION
-> While defining a function in python, we need to follow the below set of rules:
    1. the 'def' keyword is used to start the function definition
    2. the 'def' keyword is followed by a function-name which is follwed by parentheses containing the arguments passed by the user and a colon at the end
    3. after adding the colon, the body of the function starts with an indented block in a new line
    4. the return statement sends a result object back to the caller. a return statement with no argument is equivalent to retun none statement 

syntax:  def function_name(a1,a2,a3,a4...) #PARAMETERS
         return

To execute a function, we must call it. Only when it is specifically called, a function will execute and give the required output
There are two ways in which we can call a function, after we have defined it.
we can either call it from another function or we can call it from the python prompt

Eg: #defining a function that will print the passed string
    def print_output(str):    
        print(str)
        return  #will not  give any value and return to the line where it is called means it will return to function calling
    
    #calling the function
    print_output("welcome to world of python)
    
FUNCTION DEMO
1. WITH PARAMETER 
def print_output(str1):   # str IS PARAMETER
    # function statements
    print("the parameter given to function: ",str1)
    return

# to call this function for execution
input1=input("Enter user name:")   
print_output(input1)   # input IS ARGUMENT

# User enter username --> assigned to input --> input assigned to str1 on function call --> executed

input is the actual parameter because it is the real value sent to the function
str1 is known as formal parameter as it is a formality of copying value of actual parameter to formal parameter

2. WITHOUT PARAMETER

def print_output():   
    # function statements
    input1=input("Enter user name:")
    print("the parameter given to function: ",input1)
    return

# to call this function for execution 
print_output()   

** By using parameter we have to write statements for functioning outside the function block but when not using parameter we have to write it inside the function 

ques 1. how are parameters passed in a function?
all parameters (argument) in python language are passed by reference , means the same value memories are shared.....the change also reflects in calling

# Function definition is here
def func1( mylist ): 
    print ("Values inside the function before change: ", mylist)    #[10, 20, 30]
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)     #[10, 20, 50] -->> due to it is passed by refrence
    return
# Now you can call function func1() as follows: 
mylist = [10,20,30] 
func1(mylist)
print ("Values outside the function: ", mylist)   #[10, 20, 50] 

ques 2. sum of two numbers
#declaration
def sum_of_numbers(x,y):
    sum=x+y   #life of scope of variable total is inside function....so printing it outside the function will give error
    print("the sum is: ",sum)
    return 
#calling
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum_of_numbers(a,b)

but if you return sum it will go to the line where it was called form,i.e, 97 so storing the value of sum to some variable will not give error
so , that is :

#declaration
def sum_of_numbers(x,y):
    sum=x+y   
    print("the sum is: ",sum)
    return sum
#calling
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
value=sum_of_numbers(a,b)
print("the sum is: ",value)

* Types of Arguments (in Function Calls)

1. Positional Arguments
These arguments are passed in the order the parameters are defined

2. Default Arguments
These arguments are those that use the default value specified in the function definition when no explicit argument is passed.
in case user fails to give neccessary argument defult values of arguments will be taken
Eg:
#declaration
def sum_of_numbers(x=5,y=10):  # the second default argument can have value without first having it but not vice versa......the argument should be given
    sum=x+y   
    print("the sum is: ",sum)
    return sum
#calling
value=sum_of_numbers(7)   #if this argument is not given then it will take the deafult argumment but if given it will executed accordingly
print("the sum is: ",value)
# if users do not give arguments the parameter value will be taken

3. Keyword Arguments
These arguments are passed by explicitly specifying the parameter name, allowing them to be in any order.

--> dynamically passing any number of argments **args

1 USAGE
def func1(**args):    #**args will by default act as a dictionary with key value pairs
    for key,value in args.items():
        print("The key is: ",key, " the value is: ",value)

# call function with any number of arguments
func1(name="ajay", age=20, salary=10000,degree=["BCA","MCA","MBA"])
# THIS STYLE IS KNOWN AS KETWORD ARGUMNETS

--> Dynamically give many simple arguments not in form of key value pair
we will use *args

2 USAGE
"""
def func1(*val):
    sum=0
    for i in val:
        sum=sum+i
    print("The sum is: ",sum)

# call function dynamically
func1(1,2)
func1(1,2,3,4,5,6)
func1(1,2,3,4,5,5,6,7,8)
# we use this to pass any number of arguments 
# this can also be dine:
"""
num1=int((input(" enter value 1")))
num2=int((input(" enter value 2")))
num3=int((input(" enter value 3")))
num4=int((input(" enter value 4")))
func1(num1,num2,num3,num4)
"""