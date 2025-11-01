#Python resource
#Random seeds - Random number generator are algoirthm used to generate psuedu random numbers

import random
from turtle import window_height
from unittest import result
for _ in range(10):
    print(random.randint(10,20),random.random())

def generate_random_stuff(seed=None):
    random.seed(seed)
    result = []
    for _ in range(5):
        result.append(random.randint(0,5))

    characters =  list('abc')
    random.shuffle(characters)
    result.append(characters)

    for _ in range(5):
        result.append(random.gauss(0,1))
    
    return result

print('seed none')
print(random.seed(None))
print('seed 2')
print(random.seed(1))
print(random.random())

#How to pick random number from list

l = [10,20,30,40,50]

random_index = random.randrange(0,len(l)-1)
print(l[random_index])
print(list(range(1000)))

random1 =[]

for _ in range(5):
    random1.append(l[random.randrange(len(l))])

print('---------random1------------')
print(random1)
print('---------------------')
print(random.choice(random1))



for _ in range(5):
    print(random.choices(random1,k=5))





print('----------------')
print(generate_random_stuff())




