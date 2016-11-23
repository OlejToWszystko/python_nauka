#!/usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki

# program główny

# ustalmy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy ile liczb trafił
		
for i in range(ilerazy) :
	wyniki(pobierztypy(ileliczb, maksliczba),liczby)
	
print("Wylosowane liczby : ",liczby)
