#!/usr/bin/python3

a=input("Enter the sentence")
b=a.split(" ")
c=""
end=len(b)-1
i=0
while end>=0:
    c+=b[end]+" "
    end-=1

print(c)
