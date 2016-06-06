#!/usr/bin/python3

import smtplib

s = smtplib.SMTP("172.30.42.127",25)

try:
    m="\nThis is a message"
    s.sendmail("aadarsh@gmail.com","aadarshadk@hotmail.com",m)
    print("Finished sending message")
except Exception as e:
    print("Unable to send message",es)

s.quit()
