#!/usr/bin/python3

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in a:
    b.append(i) if ((i%2)==0) else ""

print(b)
