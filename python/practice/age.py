#!/usr/bin/python3
import datetime

name = input("please give me your name:")
print("Wow! you have a nice name {}".format(name))
age = int(input("please enter your age:"))
cen=100
date=datetime.datetime.now()
year = date.year
print("The year when you will be 100 is : {}".format((year)+(cen-age)))
