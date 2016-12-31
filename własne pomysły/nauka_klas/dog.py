#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dog.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

class Dog():
	""" Prosta próba modelowania psa."""
	
	def __init__(self, name, age):
		"""Inicjalizacja atrybutów name i age."""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Symulacja, że pies siada po otrzymaniu polecenia."""
		print(self.name.title() + " teraz siedzi.")
		
	def roll_over(self):
		"""Symulacja, że pies kładzie się na plecy po otrzymaniu 
			polecenia"""
		print(self.name.title() + " teraz położył się na plecy.")
		
# Stworzenie konkretnego psa na podstawie klasy
my_dog = Dog('bąbel', 4)

# Dostęp do atrybutów konkretnego egzemplarza klasy
print("Mój pies ma na imię " + my_dog.name.title() + ".")
print("Mój pies ma " + str(my_dog.age) + " lat.")

# Wywołanie metody klasy dla konkretnego egzemplarza
my_dog.sit()
my_dog.roll_over()
