#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  survey.py
#  
#  Copyright 2016 Maciej Olejnik <maciej@maciej-pc>

class AnonymousSurvey():
	"""
	Przechowuje anonimowe odpowiedzi na pytania w ankiecie.
	"""
	
	def __init__(self, question):
		"""
		Przechowuje pytanie i tworzy pustą listę do przechowywania
		odpowiedzi.
		"""
		self.question = question
		self.responses = []
		
	def show_question(self):
		"""
		Wyświetla pytanie ankiety.
		"""
		print(self.question)
		
	def store_response(self, new_response):
		"""
		Przechowuje pojedynczą odpowiedź na pytanie z ankiety.
		"""
		self.responses.append(new_response)
		
	def show_results(self):
		"""
		Wyświetla wszystkie udzielone odpowiedzi.
		"""
		print("Oto wyniki ankiety :")
		for response in self.responses:
			print('- ' + response)	
	
