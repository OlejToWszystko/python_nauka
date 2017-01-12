#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  mpl_kwadraty.py

import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
#plt.plot(input_values, squares, linewidth=5)
#plt.scatter(input_values, squares, s=200, c=['red', 'black', 'blue', 'green', 'yellow'])

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
settings = {
		'x' : x_values,
		'y' : y_values,
		's' : 100,
		'edgecolor' : 'none',
		'c' : y_values,
		'cmap' : plt.cm.Blues,
		}

plt.scatter(**settings) 
#plt.scatter(x_values, y_values, s=10, edgecolor='none', c=y_values, cmap=plt.cm.Blues)
# Zdefiniowanie tytułu wykresu i etykiet osi.
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Kwadraty wartosci", fontsize=14)

# Zdefiniowanie wielkości etykiet
plt.tick_params(axis='both', labelsize=10, which='major')

#Zdefiniowanie zakresu dla każdej osi
plt.axis([0, 1100, 0, 1100000])


plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
