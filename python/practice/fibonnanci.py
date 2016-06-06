#!/usr/bin/python3

num=int(input("Enter the number"))

def fibonacci(start,end,maxnum):
    if(end>maxnum):
        return 0
    else:
        temp=start
        start=end
        end=start+temp
        print(start)
        fibonacci(start,end,maxnum)

start=0
end=1
fibonacci(start,end,num)
