#!/usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy

# program główny

# ustalmy trudność gry
ileliczb, maksliczba, ilerazy = ustawienia()

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy ile liczb trafił
		
for i in range(ilerazy) :
	
	typy = pobierztypy(ileliczb, maksliczba)
	trafione = set(liczby) & typy

	if trafione :
		print("\nIlość trafień:", len(trafione))
		print("Trafione liczby to :", str(trafione).strip('[]'))
	else :
		print("Brak trafień")
	
	print("\n" + "x"*40 + "\n")

print("Wylosowane liczby : ",liczby)
