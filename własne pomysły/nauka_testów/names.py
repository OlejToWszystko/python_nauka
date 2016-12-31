#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  names.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

from name_function import get_formatted_name

print("Wpisz 'q', aby zakończyć działanie programu")

while True:
	first = input("\nPodaj imię: ")
	if first == 'q':
		break
	last = input("Podaj nazwisko: ")
	if last == 'q':
		break
	
	formatted_name = get_formatted_name(first, last)
	print(formatted_name)
