#!/usr/bin/python3

num = int(input("Please enter the number"))
x = range(2,num)
a=list()
for i in x:
    if((num%int(i))==0):
        a.append(i)

print(a)
