#!/usr/bin/python3

import random

a=random.sample(range(100),random.randint(0,20))
b=random.sample(range(100),random.randint(0,20))
print(a)
print(b)
c=list(set(a)&set(b))
print(c)
