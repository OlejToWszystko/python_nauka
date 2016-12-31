#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  division.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

while True:
	a = input("Podaj pierwszą liczbę (lub 'q' - zamknij) : ")
	if a.lower() == 'q':
		break
	else:
		try:
			a = int(a)
		except ValueError:
			print("Podaj prawidłową liczbę !")
			continue
		else:
			q = False
			while True:
				b = input("Podaj drugą liczbę (lub 'q' - zamknij) : ")
				if b.lower() == 'q':
					q = True
					break
				else:
					try:
						b = int(b)
					except ValueError:
						print("Podaj prawidłową liczbę !")
						continue
					else:
						break
			if q:
				print("Wychodzę")
				break
			else:
				try:
					ans = a/b
				except ZeroDivisionError:
					print("Nie wolno dzielić przez zero!")
				else:
					print(ans)
