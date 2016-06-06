#!/usr/bin/python3

import random



a = random.sample(range(100),12)
b = random.sample(range(100),16)
print(a)
print(b)
c=set()
for i in a:
    if(i in b):
        c.add(i)

print(list(c))
