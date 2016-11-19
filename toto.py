#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

liczba = random.randint(1, 10)
print "Wylosowana liczba:", liczba
	
for i in range(3):
	print "Próba ", i+1
	odp = raw_input("Jaką liczbę od 1 do 10 mam na myśli? ")
	#print "Podałeś liczbę:" , odp

	if liczba == int(odp) :
		print "Zgadłeś !"
		print "Gratulacje"
		break
	else:
		if i+1<>3 :
			print "Nie zgadłeś ! Spróbuj jeszcze raz"
		else :
			print "Dupa ! Nie zgadłeś ! Wylosowana liczba to: ", liczba

