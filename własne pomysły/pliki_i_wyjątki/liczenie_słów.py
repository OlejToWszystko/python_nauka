#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczenie_słów.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

def count_words(filename):
	'''funkcja obliczająca ilość słów we wskazanym pliku tekstowym'''
	try:
		with open(filename) as file_object:
			content = file_object.read()
	except FileNotFoundError:
		print("Nie ma takiego pliku :" + filename)
	else:
		#obliczanie ilości słów
		words = content.split()
		mes = "Plik " + filename + " zawiera " + str(len(words)) + " słów."
		print(mes)

filenames = [
	'Dorothy.txt', 'Sherlock.txt', 'Baskerville.txt', 'abc.txt',
		]

for filename in filenames:
	print(filename)
	
for filename in filenames:
	count_words(filename)
	

		
