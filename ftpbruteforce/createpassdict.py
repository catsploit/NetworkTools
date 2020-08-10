#!/usr/bin/python3
#-*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description="Expand your txt password dictionary")
parser.add_argument('-t', '--txt', help="Password txt dictionary to use", required=True, type=str)
args = parser.parse_args()
pass_dict = args.txt
pass_set = set()

# - Original concept by @ScottTheFrog - #
with open(f'{pass_dict}', 'r') as file:
	iterable = file.readlines()
	for password in iterable:
		new_password = ""
		for pass_chr in password:
			new_password += pass_chr
			pass_set.add(new_password)
	file.close()

# - Add to output file - #
with open(f'{pass_dict.strip(".txt")}_reinforced.txt', 'w') as file:
	for password in pass_set:
		add_password = password.strip('\n')
		file.write(add_password + '\n')
	file.close()