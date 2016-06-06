#!/usr/bin/python2

import httplib

host="www.google.com"

req=httplib.HTTP(host)
req.putrequest("GET","/")
req.putheader("HOST",host)
req.putheader("User-Agent","Garbage browser: 5.6")
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response",statusMsg)
