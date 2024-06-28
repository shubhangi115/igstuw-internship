"""
example of if-elif-else block

if number is +ve -ve or zero
number=int(input("enter the number "))
if number>0:
    print(f"{number} is positive")
elif number<0:
    print(f"{number} is negative")
else:
    print(f"{number} is 0")

NESTED IF"""
num=int(input("enter the number "))
if num>=0:
    if num==0:
        print("The number is 0")
    else:
        print("The number is positive")
else:
    print("The number is negative")