#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wczytywanie_danych.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>
#  
#  

wiadomosc = "Zapisywany jest tutaj dłuższy komunikat, który będzie"
wiadomosc += "\nzapisany w paru linijkach. Zobaczę, jak to się wyświetli"
wiadomosc += "\nw terminalu."
wiadomosc += "\n\nA teraz podaj mi swoje imię : "

imie = input(wiadomosc)	

print("\nWitaj : " + imie)

wiadomosc = "Podaj liczbę, a ja powiem Ci, czy jest ona parzysta lub"
wiadomosc += " nieparzysta : "

liczba = int(input(wiadomosc))

if liczba % 2 == 0:
	print(imie + ", podana przez Ciebie liczba jest parzysta")
else:
	print(imie + ", podana przez Ciebie liczba jest nieparzysta")
	
wiadomosc = "A teraz ten program będzie działał tak długo, jak tylko "
wiadomosc += "\nzechcesz. No chyba, że wpiszesz 'koniec'... "

polecenie = ''

# flaga
active = True

while active:
	polecenie = input(wiadomosc)
	if polecenie == 'koniec':
		active = False
	elif polecenie == 'end':
		active = False
	else:
		print(polecenie)
	 
print("\nA teraz zabawa w alfabet")

alfabet_wielkie = []

for litera in range(65,91):
	alfabet_wielkie.append(chr(litera))

print('\n')	
print(alfabet_wielkie)

#teraz przepiszę alfabet

alfabet_male = []

while alfabet_wielkie:
	mala_litera = alfabet_wielkie.pop(0).lower()
	alfabet_male.append(mala_litera)

print('\n')
print(alfabet_male)

