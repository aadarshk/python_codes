#!/usr/bin/python3

import random

a=random.randint(0,9)
count=0
while True:
    ch=input("Enter your choice")
    if(ch=="exit"):
        break
    else:
        count+=1
        if(a<int(ch)):
            print("High")
        elif(a>int(ch)):
            print("Low")
        else:
            print("Awesome you found the number in {} guess".format(count))
