#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

ileliczb = int(input("Podaj ile liczb chcesz losować : "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
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
		typ = int(input("Podaj liczbę " + str(i+1) + ": "))
		if typ not in typy :
			typy.add(typ)
			i = i + 1

#print("Wylosowane liczby : ",liczby)
#print("Wytypowane liczby :",typy)
	trafione = set(liczby) & typy

	if len(trafione)>0 :
		print("\nIlość trafień:", len(trafione))
		print("Trafione liczby to :", str(trafione).strip('[]'))
	else :
		print("Brak trafień")
	
	print("\nxxxxxxxxxxxxxxxxxxxxxx")

print("\nWylosowane liczby : ",liczby)
