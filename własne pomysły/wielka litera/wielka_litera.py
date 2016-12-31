#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wielka_litera.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

def literka(wyraz, ktora):
	# tworzy listę znaków z wyrazu podanego jako pierwszy argument 
	# funkcji
	zbior_liter = [litera for litera in wyraz]
	
	# zamiana litery z pozycji 'ktora' na wielką
	zbior_liter[ ktora - 1] = zbior_liter[ ktora - 1].upper()
	
	# zwraca wartość
	slowo = ''
	return(slowo.join(zbior_liter))
	
wyraz = input("Podaj wyraz : ")
ktora = int(input("Którą literę chcesz zamienić na wielką? "))

print(literka(wyraz, ktora))
	
