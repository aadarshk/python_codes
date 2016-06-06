#!/usr/bin/python2

import urllib2

url="https://google.com"
request = urllib2.Request(url)
resp = urllib2.urlopen(request)
cookies=resp.info()['Set-Cookie']
content=resp.read()
resp.close()
print(cookies)
