#!/usr/bin/python3

import poplib,imaplib

p = poplib.POP3_SSL("www.google.com",995)

print(p.getwelcome())
p.user("aadarshadk@gmail.com")
p.pass_("")

print(p.list())

p.close()

i = imaplib.IMAP4("www.google.com",143)
i.login("aadarshadk@gmail.com","")
i.select()
t,l=i.list()
print("Response code:",t)
print(l)

t,ids = i.search(None, "ALL")
print("Response code:",t)
print(ids)
t,msg=i.fetch('1','(UID BODY[TEXT])')
print(msg)
i.close()
i.logout()
