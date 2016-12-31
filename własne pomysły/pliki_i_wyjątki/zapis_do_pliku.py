#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapis_do_pliku.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

filename = 'próba_zapisu.txt'

teksty = []

while 1:
	tekst = input("Napisz coś : ")
	teksty.append(tekst)
	czy = input("Czy chcesz coś jeszcze dodać? t/N : ")
	if czy.lower() != 't':
		break
	
with open(filename, 'a') as file_object:
	for line in teksty:
		file_object.write(line + '\n')


	
