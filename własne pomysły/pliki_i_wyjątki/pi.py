#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pi.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()
	
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()
	
print(pi_string[:52])
print(len(pi_string))

birthday = '221188'

if birthday in pi_string:
	print("Tak")
else:
	print("Nie")
