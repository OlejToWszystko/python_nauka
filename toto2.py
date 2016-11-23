#!/usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json
import time
 
# program główny

# ustalmy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

nazwapliku = nick + ".json"
losowania = czytaj_json(nazwapliku)

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy ile liczb trafił
		
for i in range(ilerazy) :
	#wyniki(pobierztypy(ileliczb, maksliczba),liczby)
	trafione = wyniki(pobierztypy(ileliczb, maksliczba),liczby)

losowania.append({
	"czas": time.time(),
	"dane": (ileliczb, maksliczba),
	"wylosowane": liczby,
	"ile": trafione
	})	

zapisz_json(nazwapliku, losowania)

print("Wylosowane liczby : ",liczby)
