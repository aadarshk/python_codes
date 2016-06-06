#!/usr/bin/python2

import httplib

h="www.infiniteskills.com"

req=httplib.HTTP(h)
req.putrequest("HEAD","/")
req.putheader("Host",h)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Status",statusCode)
print(headers)
