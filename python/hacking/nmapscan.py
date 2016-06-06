#!/usr/bin/python3

import nmap
import optparse
def nmascan(tgthost,tgtport):
    nmscan=nmap.PortScanner()
    nmscan.scan(tgthost,tgtport)
    #print(nmscan[0])
    state=nmscan[tgthost]['tcp'][int(tgtport)]['state']
    print("* {} tcp/{} {}".format(tgthost,tgtport,state))

def main():
    parser = optparse.OptionParser(usage="usage: %prog [-H] <target host> -p <target port>")
    parser.add_option('-H',dest='tgtHost',type='string',help="Specify the host name")
    parser.add_option('-p',dest='tgtPort',type='string',help="Specify the port name seperated by comma")
    (options,args)=parser.parse_args()
    tgthost=options.tgtHost
    tgtports=str(options.tgtPort).split(',')
    if(tgthost==None)or(tgtports==None):
        print(parser.usage)
        exit(0)
    for tgtport in tgtports:
        nmascan(tgthost,tgtport)

if __name__=='__main__':
    main()
