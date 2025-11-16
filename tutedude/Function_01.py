#Advantages of functions
    #to avoid repetion
    #to make code reusable
    #to improve structure and readablity
    #to make function easier

#type of functions
'''

'''
def greet_user(name):
    print("Hello, welcome {}".format(name))

def greet():
    print("welcome to the python function")

greet()
greet_user('Mithun')


def add(a,b):
    return a+b;

def greet_default(name="Mithun"):
    print(f" Entered name is {name}")


def student(name, age):
    print("name is {} and age is {}".format(name,age))

print("sum is ", add(5,1));

a1 = int(input("Enter value 1"))
b1 = int(input("Enter value 2"))
sum =  add(a1,b1)
print("sum of value 1 and value 2 ", str(sum))

#default argument
print(greet_default());
#keyword argument
student(name='Mithun',age=15)
def student_info(name,age,city):
    print(f"Name:{name} Age:{age} City:{city}")

student_info(age=  24, city="New", name="Mithun")


#argbitory argument functions - it is used when you don't know arguments

def add_all(*numbers):
    total =0
    for num in numbers:
        total = total+ num
    return total;

print(add_all(1,2,4,5));
