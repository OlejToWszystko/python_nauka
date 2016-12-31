#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  my_cars.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

from car import Car
from electric_car import ElectricCar

my_car = Car('Jeep', 'Liberty', 2005, 101000)
print(my_car.get_descriptive_name())
# Zmiana wartości atrybutu egzemplarza bezpośrednio w egzemplarzu
#my_car.odometer_reading = 101000
# Uaktualnienie wartości atrybutu egzemplarza za pomocą metody
my_car.update_odometer(90000) 
my_car.read_odometer()
my_car.increment_odometer(1000)
my_car.read_odometer()

print("\nTestowanie dziedziczenia klasy\n")

my_Tesla = ElectricCar("tesla", "model s", "2016", 100, 90)
print(my_Tesla.get_descriptive_name())
my_Tesla.update_odometer(300)
my_Tesla.read_odometer()
my_Tesla.battery.describe_battery()
my_Tesla.battery.get_range()
