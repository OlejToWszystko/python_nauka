#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

class Car():
	"""Prosta próba zaprezentowania samochodu"""
	
	def __init__(self, make, model, year, odometer_reading = 0):
		"""Inicjalizacja atrybutów opisujących samochód"""
		self.make = make 
		self.model = model
		self.year = year
		self.odometer_reading = odometer_reading
	
	def get_descriptive_name(self):
		"""Zwrot elegancko sformatowanego opisu samochodu"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""Odczytuje przebieg pojazdu"""
		print(
			"Ten samochód ma przejechane " + str(self.odometer_reading) 
			+ " mil"
			)
	
	def update_odometer(self, mileage):
		"""Uaktualnia przebieg pojazdu. Uniemożliwia cofnięcie
		licznika"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Cofnięcie licznika jest niemożliwe !!!")
			
	def increment_odometer(self, trip):
		"""Zwiększa stan licznika"""
		if trip >= 0:
			self.odometer_reading += trip
		else:
			print("Cofnięcie licznika jest niemożliwe")
			

	
		

