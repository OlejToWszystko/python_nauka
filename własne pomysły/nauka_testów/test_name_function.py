#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  test_name_function.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""
	Testy dla programu 'name_function.py'
	"""
	
	def test_first_last_name(self):
		"""
		Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo
		"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
		
	def test_first_last_middle_name(self):
		"""
		Czy dane w postaci 'Wolfgang Amadeus Mozart' są obsługiwane
		prawidłowo?
		"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
		

unittest.main()
