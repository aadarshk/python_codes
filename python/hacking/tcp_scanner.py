#!/usr/bin/python3

import optparse
from socket import *
from threading import *

screenLock=Semaphore(value=1)
def connscan(tgthost,tgtport):
    try:
        conn = socket(AF_INET,SOCK_STREAM)
        conn.connect((tgthost,tgtport))
        conn.send(b"Hi")
        result=conn.recv(1024)
        print("Sucessfull Tcp open")
        screenLock.acquire()
    except Exception as e:
        screenLock.acquire()
        print(e)
    finally:
        screenLock.release()
        conn.close()

def portscan(tgthost,tgtport):
    try:
        tgtip=gethostbyname(tgthost)
    except Exception as e:
        print("Cannot resolve ip address")
        return
    try:
        tgtname=gethostbyaddr(tgtip)
        print("scan results: {}".format(tgtname))
    except:
        print("scan results: {}".format(tgtip))
    setdefaulttimeout(1)
    for ports in tgtport:
        print("scanning port: {}".format(ports))
        t = Thread(target=connscan, args=(tgthost, int(ports)))
        t.start()

def main():
    usage = "usage: %prog -H <target Host> -P <target port>"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-H',dest='tgtHost',type='string',help="provide the hostname which is our target")
    parser.add_option('-P',dest='tgtport',type='string',help='enter the port number')
    (options,args)=parser.parse_args()
    print(args)
    tgthost=options.tgtHost
    tgtport=str(options.tgtport).split(',')
    if(tgthost== None or tgtport[0]==None):
        print("Enter the details properly")
        exit(0)
    portscan(tgthost,tgtport)

if __name__ == '__main__':
    main()
