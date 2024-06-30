"""
recap:
function arguments:
1. simple positional
2. keyword
3. dynamic number of arguments *args and **args"""

"""
*RECURSION IN FUNCTIONS:
Re-currence of calling self by the function
Calling self repeatively by a function -->Recursion

SYNTAX: def func1(arg1,arg2):
            # statements
            # statements
            func1(v1,v2)   # will self call itself 
# you will move out

QUES 1. Factorial without recursion

num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("Cannot calculate the factorial of a negative number.")
else:
    i = num
    while i >= 1:
        fact = fact * i
        i = i - 1
    print(f"The factorial of {num} is: {fact}")


with factorial

def cal_recu(num):
    if (num==1) or (num==0):
        return 1
    elif num<0:
        print("can't evaluate")
    else:
        return(num*cal_recu(num-1))
num=int(input("enter a number:"))
result=cal_recu(num)
print(result)
# working --> 5*cal_rec(4) ->5*4*cal_rec(3) ->5*4*3*cal_rec(2) ->5*4*3*2*cal_rec(1)
# 5*4*3*2*1 ->5*4*3*2 ->5*4*6 ->5*24 ->120

# NONE is a special value which is returned when nothing can be calculated and returned by the function
 
QUES 2. Use recursion to calculate sum of n numbers
"""
def func_sum(n):
    if n<=1:
            return n
    else:
          return n+ func_sum(n-1)  
n=int(input("enter the number: "))
if n<=0:
      print("can't calculate")
else:
      result=func_sum(n)
      print("the sum is: ",result)
    