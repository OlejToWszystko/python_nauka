#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Trzy liczby

import sys

op = "t"

while op=="t":
	while 1:
		try:
			zbior = input("Podaj trzy liczby rozdzielone przecinkami: ").split(",")
			zbior = [int(i) for i in zbior]
			break
		except:
			print("Błędne dane!")
			if input("Kontynuować T/n ?").lower() == "n":
				sys.exit()
	
	print("Wprowadzone liczby:",zbior)
	print("\nNajmniejsza :", min(zbior))
	
	op = input("jeszcze raz ? t/N: ")
	
print("Bye, bye...")
