#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  user_class.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

class User():
	""" Klasa tworząca użytkownika"""
	
	def __init__(self, first_name, last_name, age, city):
		"""Inicjalizacja atrybutów firs_name i last_name, itd."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.city = city
		
	def describe_user(self):
		"""Wyświetla podsumowanie o użytkowniku"""
		print(
				"\tImię : " + self.first_name + "\n" +
				"\tNazwisko : " + self.last_name + "\n" +
				"\tWiek : " + str(self.age) + "\n" +
				"\tMiasto : " + self.city.title() + "\n"
				)
				
	def greet_user(self):
		"""Wyświetlenie spersonalizowanego powitania"""
		print(
				"Witaj, " + self.first_name.title() + ' ' +
				self.last_name.title() + " !\n"
				)

# Utworzenie listy egzemplarzy w pętli

users = []

while 1:
	imie = input("Podaj imię : ")
	nazwisko = input("Podaj nazwisko : ")
	wiek = int(input("Podaj wiek : "))
	miasto = input("Podaj miasto :")
	users.append(User(imie, nazwisko, wiek, miasto))
	czy = input("Czy chcesz dodać kolejnego użytkownika ? T/n :")
	if czy.lower() == 'n':
		break
		
# Wyświetlenie informacji o użytkownikach i powitanie ich

for user in users:
	user.describe_user()
	user.greet_user()
	
	
		
	
