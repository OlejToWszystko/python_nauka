#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  ciąg_fibonacciego.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

def fibonacci(n):
	"""
	Funkcja zwraca n-ty wyraz ciągu Fibonacciego
	"""
	
	# Dwa pierwsze wyrazy ciągu
	wyrazy = (0, 1)
	a, b = wyrazy
	
	# Obliczanie kolejnych wyrazów ciągu
	
	while n > 0:
		print(a)
		a, b = b, a+b
		n -= 1
		

n = int(input("Ile wyrazów ciągu chcesz wydrukować? : "))

fibonacci(n)
print()
print('=' * 20)

# rekurencyjnie

def fibonacci_rek(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		wyraz = fibonacci_rek(n-2) + fibonacci_rek(n-1)
		return wyraz

print(fibonacci_rek(n))

