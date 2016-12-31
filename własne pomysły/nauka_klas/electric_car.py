#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  electric_car.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

from car import Car

class Battery():
	"""Klasa reprezentująca baterię"""
	
	def __init__(self, battery_size):
		self.battery_size = battery_size 
		
	def describe_battery(self):
		"""Wyświetla pojemność baterii"""
		print(
			"Pojemność baterii wynosi : " + str(self.battery_size) +
			" kWh."
			)
			
	def get_range(self):
		"""Na podstawie pojemności akumulatora wyświetla zasięg 
		pojazdu"""
		if self.battery_size == 70:
			car_range = 240
		elif self.battery_size == 90:
			car_range = 270
			
		message_b = "Twój zasięg wynosi : " + str(car_range) + " mil."
		print(message_b)  
			
# dziedziczenie - klasa potomna

class ElectricCar(Car):
	"""Przedstawia cechy charakterystyczne samochodu elektrycznego"""
	
	def __init__(
		self, make, model, year, odometer_reading = 0, battery_size = 70
		):
		"""Inicjalizacja atrybutów klasy nadrzędnej"""
		super().__init__(make, model, year, odometer_reading)
		"""Inicjalizacja atrybutów klasy potomnej"""
		self.battery = Battery(battery_size)
		
