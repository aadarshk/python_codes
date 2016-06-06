#!/usr/bin/python3

import random

a=random.sample(range(100),random.randint(0,30))
b=random.sample(range(100),random.randint(0,35))
c=[]

def first_last(x):
    c.append(x[0])
    c.append(x[-1])
    print(c)

print(a)
first_last(random.choice([a,b]))
print(b)
first_last(random.choice([a,b]))
