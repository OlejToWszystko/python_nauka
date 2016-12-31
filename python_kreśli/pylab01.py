#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pylab

def wczytaj(znak):
	while 1:
		try:
			x = int(input("Podaj " + znak + " : "))
			return x
		except:
			print("Błędne dane!")
			continue

a = wczytaj('a')
b = wczytaj('b')
x = range(-10, 11) #lista argumentów

#y = list(map(lambda i: a*i+b, x)) # lista wartości
y = [a*i + b for i in x] # lista wartości
'''for i in x:
	y.append(a * i + b)'''
	
pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x-b')
pylab.grid(True)
pylab.show()
