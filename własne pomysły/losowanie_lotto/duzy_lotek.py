#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  duzy_lotek.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

import random

def losowanie(ile, maks):
	wylosowane = []
	i = 1
	while i <= ile:
		liczba = random.randint(1, maks)
		if liczba not in wylosowane:
			wylosowane.append(liczba)
			i += 1
		else:
			continue
	wylosowane.sort()
	return(wylosowane)
	
czy_losowac = True
duzy_lotek = {}
zaklad = 1

#ile = int(input("Ile : "))
#maks = int(input("Z ilu : "))

#print(losowanie(ile, maks))


while czy_losowac:
	tak_nie = input("Czy wylosowac Ci duzego lotka ? y/N : ")
	if tak_nie == 'y':
		duzy_lotek[zaklad] = losowanie(6, 49)
		zaklad += 1
	else:
		czy_losowac = False
		
for zaklad, liczby in duzy_lotek.items():
	print(str(zaklad) + " : " + str(liczby))
	

