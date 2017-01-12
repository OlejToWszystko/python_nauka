#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  random_walk.py

from random import choice 

class RandomWalk():
	"""Klasa przeznaczona do wygenerowania błądzenia losowego."""
	
	def __init__(self, num_points=5000, x_start=0, y_start=0):
		"""Inicjalizacja atrybutów błądzenia."""
		self.num_points = num_points
		
		# Współrzędne początkowe
		self.x_start = x_start
		self.y_start = y_start
		
		# Listy ze współrzędnymi punktów
		self.x_values = [self.x_start]
		self.y_values = [self.y_start]
	
	def get_step(self):
		""""
		Ustalenie kierunku oraz długości kroku.
		"""
		step_dir = choice([-1, 1])
		step_dist = choice(list(range(5))) 
		step = step_dir * step_dist
		return step
		
	def fill_walk(self):
		"""Wygenerowanie wszystkich punktów dla błądzenia losowego."""
		
		# Wykonywanie kroków, aż do chwili osiągnięcia oczekiwanej 
		# liczby punktów
		while len(self.x_values) < self.num_points:
			# Ustalenie kierunku oraz odległości do pokonania w tym
			# kierunku
			
			x_step = self.get_step()
			
			y_step = self.get_step()
			
			# Odrzucenie ruchów, które prowadzą donikąd
			if x_step == 0 and y_step == 0:
				continue
				
			# Ustalenie następnych wartości x i y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
			 
