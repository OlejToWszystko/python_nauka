#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pong_obj.py
#  
#  Copyright 2017 Maciej Olejnik <maciej@maciej-pc>

import pygame
import pygame.locals

class Board():
	"""
	Plansza do gry. Odpowiada za rysowanie okna gry
	"""
	
	def __init__(self, width, height):
		"""
		Konstruktor planszy do gry. Przygotowuje okienko gry.
		
		:parametr width:
		:parametr height:
		"""
		self.surface = pygame.display.set_mode((width, height), 0, 32)
		pygame.display.set_caption('Single Pong')
		
	def draw(self, *args):
		"""
		Rysuje okno gry
		
		:parametr args: lista obiektów do narysowania
		"""
		background = (230, 255, 255)
		self.surface.fill(background)
		for drawable in args:
			drawable.draw_on(self.surface)
			
		# dopiero w tym miejscu następuje faktyczne rysowanie
		# w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać
		# narysowane
		pygame.display.update()


class PongGame():
	"""
	Klasa kontrolera gry. Łączy wszystkie elementy gry w całość.
	"""
	
	def __init__(self, width, height):
		pygame.init()
		self.board = Board(width, height)
		# zegar, którego użyjemy do kontrolowania szybkości rysowania
		# kolejnych klatek gry
		self.fps_clock = pygame.time.Clock()
		self.ball = Ball(20, 20, width/2, height/2)
		self.player1 = Racket(80, 20, width/2 - 40, height - 40) 
		self.player2 = Racket(80, 20, width/2 - 40, 20, color=(0, 0, 0))
		self.ai = Ai(self.player2, self.ball, self.board)
		self.judge = Judge(self.board, self.ball, self.player1, self.player2)
	
	def run(self):
		"""
		Główna pętla programu
		"""
		while not self.handle_events():
			# działaj w pętli do momentu otrzymania sygnału do wyjścia
			self.ball.move(self.board, self.player1, self.player2)
			self.board.draw(
				self.ball,
				self.player1,
				self.player2,
				self.judge,
			)
			self.ai.move()
			self.fps_clock.tick(30)
			
	def handle_events(self):
		"""
		Obsługa zdarzeń systemowych
		
		:return True jeżeli pygame przekazał zdarzenie wyjścia z gry
		"""
		for event in pygame.event.get():
			if event.type == pygame.locals.QUIT:
				pygame.quit()
				return True
				
			if event.type == pygame.locals.MOUSEMOTION:
				# myszka steruje ruchem pierwszego gracza
				x, y = event.pos
				self.player1.move(x, self.board)


class Drawable():
	"""
	Klasa bazowa do rysowania obiektów
	"""
	
	def __init__(self, width, height, x, y, color=(0, 255, 0)):
		self.width = width
		self.height = height
		self.color = color 
		self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
		self.rect = self.surface.get_rect(x=x, y=y)
		
	def draw_on(self, surface):
		surface.blit(self.surface, self.rect)


class Ball(Drawable):
	"""
	Piłęczka, sama kontroluje swoją prędkość i kierunek poruszania się.
	"""
	
	def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
		super().__init__(width, height, x, y, color)
		pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.start_x = x
		self.start_y = y
		
	def bounce_y(self):
		"""
		Odwraca wektor prędkości w osi y
		"""
		self.y_speed *= -1
		
	def bounce_x(self):
		"""
		Odwraca wektor prędkości w osi x
		"""
		self.x_speed *= -1
		
	def reset(self):
		"""
		Ustawia piłeczkę w położeniu początkowym i odwraca wektor 
		prędkości w osi y
		"""
		self.rect.center = (self.start_x, self.start_y)
		self.bounce_y()
		
	def move(self, board, *args):
		"""
		Przesuwa piłeczkę o wektor prędkości
		"""
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		
		if self.rect.x < 0 or self.rect.x + self.width > board.surface.get_width():
			self.bounce_x()
			
		if self.rect.y < 0 or self.rect.y + self.height > board.surface.get_height():
			self.bounce_y()
			
		for racket in args:
			if self.rect.colliderect(racket.rect):
				self.bounce_y()


class Racket(Drawable):
	"""
	Rakietka, porusza się w osi x z ograniczeniem prędkości.
	"""
	
	def __init__(self, width, height, x, y, color=(0, 255, 0), max_speed=10):
		super().__init__(width, height, x, y, color)
		self.max_speed = max_speed
		self.surface.fill(color)
		
	def move(self, x, board):
		"""
		Przesuwa rakietkę w wyznaczone miejsce.
		"""
		delta = x - self.rect.x
		if abs(delta) > self.max_speed:
			delta = self.max_speed if delta > 0 else -self.max_speed
		if x + self.width >= board.surface.get_width():
			self.rect.x = board.surface.get_width() - self.width
		else:
			self.rect.x += delta


class Ai():
	"""
	Przeciwnik steruje swoją rakietką na podstawie obserwacji piłeczki
	"""
	
	def __init__(self, racket, ball, board):
		self.racket = racket
		self.ball = ball
		self.board = board
		
	def move(self):
		x = self.ball.rect.centerx
		self.racket.move(x, self.board)


class Judge():
	"""
	Sędzia gry
	"""
	
	def __init__(self, board, ball, *args):
		self.ball = ball
		self.board = board
		self.rackets = args
		self.score = [0, 0]
		
		# Przed pisaniem tekstów musimy zainicjować mechanizmy wyboru 
		# fontów PyGame
		pygame.font.init()
		# pobiera ścieżkę czcionki Arial
		font_path = pygame.font.match_font('arial')
		# tworzy obiekt typu font Font(filename, size) -> Font
		self.font = pygame.font.Font(font_path, 64)
		
	def update_score(self, board_height):
		"""
		Jeśli trzeba, przydziela punkty i ustawia piłeczkę w 
		początkowym położeniu
		"""
		if self.ball.rect.y < 0:
			self.score[0] += 1
			self.ball.reset()
		elif self.ball.rect.bottom > board_height:
			self.score[1] += 1
			self.ball.reset()
			
	def draw_text(self, surface, text, x , y):
		"""
		Rysuje wskazany tekst we wskazanym miejscu
		"""
		text = self.font.render(text, True, (150, 150, 150))
		rect = text.get_rect()
		rect.center = x, y
		surface.blit(text, rect)
		
	def draw_on(self, surface):
		"""
		Aktualizuje i rysuje wyniki
		"""
		height = self.board.surface.get_height()
		self.update_score(height)
		
		width = self.board.surface.get_width()
		self.draw_text(surface, "Player: {}".format(self.score[0]), width/2, height * 0.3)
		self.draw_text(surface, "Computer: {}".format(self.score[1]), width/2, height * 0.7)
		
			
				
if __name__ == "__main__":
	game = PongGame(800, 400)
	game.run()
