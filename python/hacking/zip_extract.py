#!/usr/bin/python3

import zipfile
from threading import Thread
def extractfile(zfile,password):
    try:
        print(password)
        zfile.extractall(pwd=password)
        print("The password is {}".format(password.decode(encoding='utf-8')))
    except Exception as e:
        pass

def main():
    zfile=zipfile.ZipFile("evil.zip")
    fopen=open('dictionary.txt','r')
    for line in fopen.readlines():
        line=line.strip('\n')
        password=bytes(line,encoding='utf-8')
        #print(password)
        t=Thread(target=extractfile, args=(zfile,password))
        t.start()

if __name__ == '__main__':
    main()
