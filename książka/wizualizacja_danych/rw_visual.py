#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	rw = RandomWalk()
	rw.fill_walk()

	plt.scatter(rw.x_values, rw.y_values, s=15)
	plt.show()
	
	keep_running = input("Jeszcze raz? T/n : ")
	if keep_running.lower() == 'n':
		break 
