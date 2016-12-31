#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_writer.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

import json

numbers = [11, 22, 1988, 73, 179, 105]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
