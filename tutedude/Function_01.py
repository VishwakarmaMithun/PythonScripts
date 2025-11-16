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

print("sum is ", add(5,1));

a1 = int(input("Enter value 1"))
b1 = int(input("Enter value 2"))
sum =  add(a1,b1)
print("sum of value 1 and value 2 ", str(sum))

print(greet_default());