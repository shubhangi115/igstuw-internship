"""
Python data types are categorized into two as follows:
* Mutable data types: data types where the value assigned to a variable can be changed
eg: dictionaries
    lists
    sets
* Immutable data type: data types where the value assigned to a variable can't be changed
eg: number
    strings
    tuples

STRINGS:
collection of characters enclosed in quotes.

two types of string literals:
-> single line- terminated with single line
-> multi line strings- written in multiple lines.
There are two ways of creating multiline srings:-
1. by adding a back slash at the end of each string. "\"
2. using triplle quotation marks. '""" """''

eg:
str1= 'hello welcome'  #will print this only
print(str1)
str2="hello" \   # '\' is connector      
    "welcome" 
print(str2)  # will print string without space
str3='''hello
welcome'''
print(str3)  # will print string as it is writen,i.e, with next line

SLICING INDEX
str[starting_index_pos:stop_index_pos:No. of moves or jump]
str="Hello all"
str[1:5]  # will print 1 to len-1,i.e, 4

NOTE-str[:] default 0 to len of string
     str[:5] default 0 to given ,ie., 5

# Negative slicing
str1="Hello all"
print(str1[-5:-1]) 
print(str1[-1:-5])
print(str1[-7::2])
print(str1[::-1])

name="Aditya"
str=name[::-1]   #----> reversing whole string
print("reverse ",str)
str= name[-4:-1:-1] #------>error......opposite in direction of flow
print("1 ",str)
str= name[1:4:-1] #-------> same error
print("2 ",str)
str= name[-1:-4:-1] #------>> dity
print("3 ",str) 
str= name[1:-1:1]
print("4 ",str)
str= name[-4:1:1]
print("5 ",str)        
str= name[-4:1:-1]
print("6 ",str)
str=name[:]
print("7 ",str)

strings are immutable
str1='k'

STRING COMPARISON-- gives true/false

#>,<,== -> to check for equality
# str1 = "Hello"
# str2 = "hello"
# print(str1 == str2)
# print(str1>str2)
# print(str1< str2)

#Ascii codes
#A-Z = 65 to 90
#a-z =97-122
#ord() -> gives ascii value of char
#chr() -> gives corresponding chars for a given ascii code

# print(ord("H"))
# print(ord("h"))
# print(chr(65))
# print(chr(97))


STRING REPITION

#*operator to reapeat string multiple times

# str1 = "Hello"
# print(str1*2) 
# print(str1*5)

CONCATATINATION OPERATOR

str1 = "Hello"
str2 = " "
str3 = "All"
print(str1+str2+str3)

Find length or number 

str1 ="Hello all"
print("The no. of characters in string are :",len(str1))

MEMBERSHIP OPERATOR-- give true/false
'in' and 'not in' operator
str1= "hello welcome"
print('llo' in str1)
print('....'not in str1)

STRING METHODS

1. upper and lower

str1="hello all"
print(str1.upper())
print(str1)
print(str1.lower())

2. replace a particular sub-string inside a string to create a new string

str1="hello all"
new_string=str1.replace('all','all the')
print("original string ",str1)
print("new string ",new_string)

3. give the index number of first occurence of value given, gives -1 when not present

str1="hello all"
print(str1.find('s')) 

4. returns index of substring, will give error when not found the substring

str1="hello all"
print(str1.index('s'))   # will give error
print(str1.index('h')) 

5. to slice or split or cut the string 
split()--- will make list out of it
splits using separator and default sep is ' ' 
str1="hello all in the class"
print(str1.split()) 
str1="hello all, in the class"
print(str1.split(',')) 
str1="hello all in the class"
print(str1.split(',',1)) # to restrict 1 time splitting 

syntax: split(separator '', max number of split)

6. to remove spaces from text string specific leading and trailing
strip()

str1="    hello    all     in the class     "
print(str1.strip()) 

# remove space from first
print(str1.lstrip()) 

# remove space form last
print(str1.rstrip()) 

"""




