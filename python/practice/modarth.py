#!/usr/bin/python3

def oddoreven(num):
    if(num==0):
        print("The number is neither odd nor even")
    elif((num%2)==0):
        print("The number is an even number")
    else:
        print("The number is an odd number")

def divisible(num):
    if((num%4)==0):
        print("The number is divisible by 4")
    else:
        print("The number is not divisible by 4")

def num_div(num,div):
    if((num%div)==0):
        print("The number {} is perfectly divisible by {}".format(num,div))
    else:
        print("The number {} is not divisible by {}".format(num,div))

if __name__ == '__main__':
    arg = input("Enter your choice \n 0.do all the below \n 1.odd or even \n 2.divisble by 4 \n 3.check if divisble by a number \n 4. exit")
    if(int(arg)==0):
        oddoreven(int(input("Enter the number to check oddoreven: \n")))
        divisible(int(input("Enter the number to check divisblity by 4: \n")))
        num_div(int(input("enter the number: \n")),int(input("enter the div number: \n")))
    elif(int(arg)==1):
        oddoreven(int(input("Enter the number to check oddoreven: \n")))
    elif(int(arg)==2):
        divisible(int(input("Enter the number to check divisblity by 4 \n")))
    elif(int(arg)==3):
        num_div(int(input("enter the number: \n")),int(input("enter the div number \n")))
    else:
        exit()
