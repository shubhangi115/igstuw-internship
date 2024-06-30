"""
-> an exception is an event, which occurs during the execution of a program and interripts its usual flow
-> an exception is a pyhton object that represents an error situation
-> when an execption is raised, it must be handled to prevent the undesored termination of program
-> when an exception as we call it, python will normally stop and generate an error message
-> these exception can be handled using the try statement. since the try block raises an error, the except block will be executed
Syntax: try: 
            lines of code that may raise an exception
        except Exception 1:
            if Exception 1 occurs, execute this block of code
        except Exception 2:
            if Exception 2 occurs, execute this block of code
        else: 
            if no exception occurs
# the finally block lets you execute code, regardless of the result of the try and except blocks

# HOW TO VIEW ALL THE BUILT-IN EXCEPTION

print(dir(locals()['__builtins__']))  #here "dir" is directory--> return a file
# directory of all error we can have

ARTHIMETICS ERROR

try: 
    lines of code that may raise an exception
except Exception 1:
   if Exception 1 occurs, execute this block of code
except Exception 2:
    if Exception 2 occurs, execute this block of code
except:
    this will be general except block for any exception
else: 
    if no exception occurs
finally:
    this statements will work always after try-except-else have completed working

eg: num/0 -> infinity
# print("division: ",100/0) #ZeroDivisionError

n1=int(input("enter numerator: "))
n2=int(input("enter denominator: "))
div=n1/n2
print("the result is: ",div)

# list1=[1,2,3,4,5]
# print(list1[5])     #IndexError

try:
    n1=int(input("enter numerator: "))
    n2=int(input("enter denominator: "))
    div=n1/n2
    print("the result is: ",div)
    list1=[1,2,3,4,5]
    i=int(input("enter index value: "))
    print(list1[i]) 
    print("enter number", num)
except ZeroDivisionError:
    print("cannot divide by zero")
except IndexError:
    print("can't access elements beyond length")
except:
    print("an exception occured.....please check inputs again")
else:
    print("no exception occured!! successful execution")
finally:
    print("inside finally block....")
    user=input("enter user name")
    print(f"welcome {user}")

NOTE : 1. WHEN ERROR OCCURS THEN THAT "except" BLOCK WILL EXECUTED AND ELSE "will" BE IGNORED
       2. AND WHEN ERROR DO NOT OCCUR THEN "except" BLOCK WILL NOT BE EXECUTED AND "else" WILL BE EXECUTED
       3. WHEN WE TRY TO EXECUTE SOMETHING THAT DON'T COMES UNDER THE EXCEPTION MENTIONED IN THE CODE THEN generic "except" WILL BE EXECUTED
          Eg: in line

USER DEFINED EXCEPTIONS
QUES. HOW TO CREATE OUR OWN USER-DEFINED EXCEPTION
--> CREATE A NEW USER CLASS WHICH IS DERIVED FRO EXCEPTION CLASS
For eg: create exception for retired senoir citizen candidates"""
class InvalidAgeCalException(Exception):  # "Exception" is parent class....sabko dada
    pass
age=int(input("enter a relavant age for retired employee:"))
try:
    if age<60:
        raise InvalidAgeCalException
    else:
        print("valid age")
        print("the employee is eligible for pension......")
except InvalidAgeCalException:
    print("exception occurred!!")