#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  name_function.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

def get_formatted_name(first, last, middle=''):
	"""
	Generuje elegancko sformatowane imię i nazwisko
	"""
	if middle:
		full_name = first + ' ' + middle + ' ' + last 
	else:
		full_name = first + ' ' + last 
	return full_name.title()
