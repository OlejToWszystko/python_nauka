#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_reader.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

import json

filename = 'numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
