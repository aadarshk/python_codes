#!/usr/bin/python3

import passlib.hash,crypt

def test_pass(passw_crypt,user):
    salt=passw_crypt.split("$")[2]
    print(salt)
    dopen=open('dictionary.txt','r')
    for word in dopen.readlines():
        word=word.strip("\n")
        x=passlib.hash.sha512_crypt.encrypt(word,salt=salt,rounds=5000)
        #print(x)
        #print('\n')
        if(x==passw_crypt):
            print("{} has a password:{}".format(user,word))
            return
    print("{} password not found".format(user))


def main():
    fopen=open('password.txt','r')
    for line in fopen.readlines():
        user=line.split(":")[0]
        passw=line.split(":")[1].strip(' ')
        test_pass(passw,user)


if __name__ == '__main__':
    main()
