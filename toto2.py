#!/usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json, czytaj_str, zapisz_str
import time
 
# program główny

# ustalmy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

nazwapliku = nick + ".json"
nazwapliku2 = nick + ".txt"
losowania = czytaj_json(nazwapliku)
losowania2 = czytaj_str(nazwapliku2)

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy ile liczb trafił
		
for i in range(ilerazy) :
	#wyniki(pobierztypy(ileliczb, maksliczba),liczby)
	trafione = wyniki(pobierztypy(ileliczb, maksliczba),liczby)

	losowania2.append({
		"czas": time.time(),
		"dane": (ileliczb, maksliczba),
		"wylosowane": liczby,
		"ile": trafione
		})	

losowania.append({
	"czas": time.time(),
	"dane": (ileliczb, maksliczba),
	"wylosowane": liczby,
	"ile": trafione
	})
		
zapisz_json(nazwapliku, losowania)
zapisz_str(nazwapliku2, losowania2)

print("Wylosowane liczby : ",liczby)
