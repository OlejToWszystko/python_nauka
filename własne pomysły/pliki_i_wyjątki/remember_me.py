#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  remember_me.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc

import json

def get_stored_usernmae(filename):
	'''Funkcja pobiera nazwę użytkownika z pliku json 
	(o ile istnieje)'''
	
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		

def get_new_username(filename):
	"""
	Funkcja pobiera od użytkownika jego nazwę użytkownika 
	i zapisuje w pliku zewnętrznym
	"""
	
	username = input("Podaj swoją nazwę użytkownika : ")
	
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	
	return username
		

def greet_user(filename):
	"""Funkcja witająca użytkownika"""
	
	username = get_stored_usernmae(filename)
	
	if username:
		print("Witamy ponownie, " + username + " !")
	else:
		username = get_new_username(filename)
		print("Witamy pierwszy raz, " + username + " !")
		
filename = 'user.json'
greet_user(filename)
