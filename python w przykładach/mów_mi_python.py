#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Mów mi python

aktRok = 2016
pythonRok = 1990

wiekPythona = aktRok - pythonRok

imie = input("Jak masz na imię?")
wiek = int(input("Ile masz lat"))

print("Witaj!\nMam na imię Python, mam", wiekPythona, "lat.")
print("Witaj w moim świecie",imie)

if wiekPythona > wiek:
	print("Jesteś młodszy ode mnie")
else:
	if wiekPythona == wiek:
		print("Mamy tyle samo lat")
	else:
		print("Jesteś starszy ode mnie")

