'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


 
FibArray = [0, 1]
 
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
 
# Driver Program
 
print(fibonacci(8))



# ! Eg:4
# ? function with return statement

# Return

#1.) A variable declared inside the function can be accessed outside the function
# Using return
#2.)Return does not print anything
#3.) We cannot write any code below return statement

# def f1():
#     z = 8
# f1()
# print(z) # error ---> cannot use outside the function


def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj = f1(6,8)
obj = f1(4,6)

def gracemark(object):
    print(output+4)
gracemark(obj)
gracemark(obj1)


# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value:"))
palindrome(a)

# ? Bsed on the declaration of parameter and args
# ? Functiuon are divided into 6 catagories

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args



# ? Positional args

# Eg:1
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {}marks."
    print(txt.format(name,phone,mark))

profile(8978011959,"ABHI",60) # unexpected output



# * keyword args
# ! Eg:2
# ? To overcome the disadvantages of position args, we use keyword args
# ? It is the process of initialising the parameter with the args while calling the
# ? Function

def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {}marks."
    print(txt.format(name,phone,mark))

profile(name = "abhi", mark=60,phone=8008554769)

# Todo---> Exception of keyword args function

def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {}marks."
    print(txt.format(name,phone,mark))

profile(name = "abhi", 12345678,mark=60)# error---> positional args follow keywordargs
profile(12345678,name="Abi",mark=60)# error ---> name has multiple values
profile("abi", maark=60,phone=12345678)

# * Default args
# The method of assigning the argument to the parameter while declaring the
# function

# ! Eg:1

def profile(name,phone,place="kadapa"):
    txt = "my name is {}. my phone number is {}. I got {}marks."
    print(txt.format(name,phone,place))
    
profile("abi",12345678)



# ! Eg:2
def profile(name,phone,place="kadapa"):
    if place == "kadapa" or place=="kadapa" or place=="kadapa":
        txt = "my name is {}. my phone number is {}. I got {}marks."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("abi",12345678)

Exception
def profile(name,place="kadapa",phone): # error---> coz default args should not follow
                                    # positional param
    if place =="kadapa" or place=="kadapa" or place=="kadapa":
        txt = "my name is {}. "my phone number{}. I am from {}."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("abi",1234567)

# * Variable length params

# ! Eg:1
# To pass more than 1 arg to a parameter means we use variable length args
# To convert normal paremeter to variable length param,add * to their prefix of paran

# name = "abi",'name2', 'name3'
def profile(*name):
    print("my name is ",name)
profile("abi",'name2','name3')


# Eg:2
def profile(*name,age):
    for val in name:
        print("my name is",val,"may age is",age)
profile("abi",'name2','name3',28) #erroe---> age has no args


def profile(age,*name):
    for val in name:
        print("my name is", val,"may age is ",age)
profile(28,"abi",'name2','name3')



# * Keywords variable length args
# Kwargs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
def price(**price_list):
    print(price_list)
print(shirt=1000,iphone=80000)


d1 = {"a":100,"b":200,"c":300}
d1 = dict(a=100, b=200,c=300)
print(d1)
   

# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


d={}
for x in range(1,6):
    d.update({x:x**2})
print(d)

n = int(input("Enter the number:"))

def dict(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val]= val**2
    print(d1)
dict(5)

# ! ------> Object oriented programming
# The paradigms of object oriented progrmming are

# class
# objects
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation


# ! class is a blue print of an object

l1 = [1,2,3,4,5,6]


# ? Eg:1
class c1:
    name1 = "Abhi"
    print(name1)

# ? Eg:2
class person:
    name = "Abhi"
c = person() # c os object
# The process of creation of an object is called as Instantiation
print(c.name)

# ? Eg:3
# create of a method
# When the function is created with a class is called as method


# ! Method without parameter
class person:
    def display(person): # It is a method
        print("Hello welcome to classes")
p = person()
p.display()

# ! Eg:4
# ! Method with parameter
class person:
    def display(person,name,age):
        print(name,age)

p = person()
p.display("Abhi",28)
'''

# ! Eg:5
class person1:
    fname3 = "Abhi" # Attribute of static variable
    lname = "T"

    def first_name(self):
        print(self.name3)

    def full_name(self):
        print(self.fname+" "+self.lname)

p = person1()
p.fist_name()
p.full_name()

tuple

    
    
    




    
