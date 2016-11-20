#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

try :
	
	ileliczb = int(input("Podaj ile liczb chcesz losować : "))
	maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
	if ileliczb > maksliczba :
		exit("Błędne dane!")
except :
	exit("Błędne dane!")

liczby = []

i = 0

while i<ileliczb :
	liczba = random.randint(1, maksliczba)
	if liczby.count(liczba)==0 :
		liczby.append(liczba)
		i = i + 1
		
for n in range(3) :
	

	print("Wytypuj", ileliczb, "z", maksliczba, "liczb")
	typy=set()

	i = 0

	while i<ileliczb :
		try :
			typ = int(input("Podaj liczbę " + str(i+1) + ": "))
		except ValueError :
			print("Błędne dane")
			continue
			
		if 0 < typ <= maksliczba and typ not in typy :
			typy.add(typ)
			i = i + 1

	trafione = set(liczby) & typy

	if len(trafione)>0 :
		print("\nIlość trafień:", len(trafione))
		print("Trafione liczby to :", str(trafione).strip('[]'))
	else :
		print("Brak trafień")
	
	print("\n" + "x"*40 + "\n")

print("Wylosowane liczby : ",liczby)
