"""
Variable scope: A vriable scope is the region or area where the variable can be accessed and used
Lifetime: it is the number of lines of code till that variable is used

Types of scope of variable:
1. Local variable
2. global variable
3. non local variable

1. Local scope of variable
def fun(): 
    result="final message isside"  #result is a local variable
    print("the result is: ",result)
    # result can be accessed inside the block of function fun()
fun() # calling func outside
print("the result is: ",result) # not accessible outside fun

2. Global scope of variable

result="message outside the function scope"   # it is outside the function so it is accessible 
def func():
    result="local result inside func()"  # local scope as it is present in func()
    print("calling result inside the func(): ",result)
    # lifetime of local result variable is 2 lines 22-23
    # local scope always overwrite global scope
    
# come outside the func
func()
print("calling result outside func(): ",result)
# lifetime of global variable is 18-27

3. Non-local scope of variable --> they are used in context of nested function such that these variables cannot be assumed to be in local or global

def func_outer():
    result="inside func_outer()"  # local for outer and global for inner
    print("the result is: ",result)

    # created a nested function
    def func_inner():
        # result="hello" #if this line is written then the output for this function will be this result ,i.e, "hello" 
        print("the result is: ",result)
    
    #come outside func_inner()
    print("calling inner func()")
    func_inner()

#come outside func_outer()
print("calling outer func()")
func_outer() 

but what if we want that agar func_inner() mein hamnein jo result ki value change ki thi vo baaki result mein bhi show hoye vo ek alag variable na bne aur na shadow kre pehle vaale result ko ?
to hum use karenge "nonlocal" key word jisse jahan se hum ye keyword use kr rhe hai uske baad se result ki value change ho jaayegi """

def func_outer():
    result="inside func_outer()"  # local for outer and global for inner
    print("the result is: ",result)

    # created a nested function
    def func_inner():
        nonlocal result
        result="hello" 
        print("the result is: ",result)
    
    #come outside func_inner()
    print("calling inner func()")
    func_inner()
    print("result in func_outer and inner is: ",result)

#come outside func_outer()
print("calling outer func()")
func_outer()