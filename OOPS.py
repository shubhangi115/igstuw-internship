""" 
Python is an object oriented programming language
It allows us to develop applications using an object oriented approach using classes and objects
Some OOPs concepts:

* OBJECTS:
1. The are the basic run time entities in an object oriented system
2. They may represent a person, a place , a bank account, a table of data or any item that the program must handle
3. When a program is executed the object interact by sending messages to one another
4. Objects have two components:
   - Data (i.e. attributes)
   - Behaviors (i.e. methods) """

# class and instantiate the objects

# Define a new class user-defined class
# class keyword
class employee:
    # define variables or attribute or properties of class
    emp_id=0
    emp_sal=0.0
    #define methods of class
    # self parameter inside method suggests thst this metho can be only with the current object of the related class
    def emp_details(self):
        print(f"the emp_id is: ",{self.emp_id})