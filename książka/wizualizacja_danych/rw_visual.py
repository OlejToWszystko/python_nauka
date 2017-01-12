#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	settings = {
			'x' : rw.x_values,
			'y' : rw.y_values,
			's' : 1,
			'c' : list(range(rw.num_points)),
			'cmap' : 'Accent',
			'edgecolor' : 'None',
			}
	
	# ustawienia punktu początkowego
	settings_0 = {
			'x' : rw.x_values[0],
			'y' : rw.y_values[0],
			's' : 100,
			'c' : 'green',
			'edgecolor' : 'None',
			}
	
	# ustawienia punktu końcowego
	settings_end = {
			'x' : rw.x_values[-1],
			'y' : rw.y_values[-1],
			's' : 100,
			'c' : 'red',
			'edgecolor' : 'None',
			}
			
	# określenie wielkości okna wykresu
	plt.figure(figsize=(10, 6), dpi=128)

	plt.scatter(**settings)
	plt.scatter(**settings_0)
	plt.scatter(**settings_end)
	
	# ukrycie osi
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running = input("Jeszcze raz? T/n : ")
	if keep_running.lower() == 'n':
		break 
