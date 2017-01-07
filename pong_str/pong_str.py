#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pong_str.py
#  
#  Copyright 2017 Maciej Olejnik <maciej@maciej-pc>

import pygame
import sys
from pygame.locals import *

# inicjacja modułu pygame
pygame.init()

# szerokość i wysokość okna gry
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400

# kolor okna gry, składowe RGB zapisane w tupli
LT_BLUE = (230, 255, 255)

# powierzchnia do rysowania, czyli inicjacja pola gry
oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)

# tytuł okna gry
pygame.display.set_caption('Prosty Pong')

# paletka gracza #############################################
PALETKA_SZER = 100
PALETKA_WYS = 20
BLUE = (0, 0, 255) # kolor wypełnienia
PALETKA_1_POZ = (350, 360) # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem
paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1.fill(BLUE)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

# paletka ai ##################################################
RED = (255, 0, 0)
PALETKA_AI_POZ = (350, 20) # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem
paletkaAI = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletkaAI.fill(RED)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
paletkaAI_prost = paletkaAI.get_rect()
paletkaAI_prost.x = PALETKA_AI_POZ[0]
paletkaAI_prost.y = PALETKA_AI_POZ[1]
# szybkość paletki AI
PREDKOSC_AI = 5

# piłka #######################################################
P_SZER = 20 # szerokość
P_WYS = 20 # wysokość
P_PREDKOSC_X = 6 # prędkość pozioma x
P_PREDKOSC_Y = 6 # prędkość pionowa y
GREEN = (0, 255, 0) # kolor piłki
# utworzenie powierzchni piłki, narysowanie piłki i wypełnienie kolorem
pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka, GREEN, [0, 0, P_SZER, P_WYS])
# ustawienie prostokąta zawierającego piłkę w początkowej pozycji
pilka_prost = pilka.get_rect()
pilka_prost.x = OKNOGRY_SZER / 2
pilka_prost.y = OKNOGRY_WYS / 2

# ustawienie animacji #########################################
FPS = 30 # liczba klatek na sekundę
fpsClock = pygame.time.Clock() # zegar śledzący czas

# komunikaty tekstowe ##########################################
# zmienne przechowujące punkty i funkcje wyświetlające punkty
PKT_1 = '0'
PKT_AI = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64) # czcionka komunikatów


def drukuj_punkty(punktacja, poz_x, poz_y, okno):
	tekst = fontObj.render(punktacja, True, (0, 0, 0))
	tekst_prost = tekst.get_rect()
	tekst_prost.center = (poz_x, poz_y)
	okno.blit(tekst, tekst_prost)
	
# pygame.key.set_repeat() - control how held keys are repeated	
pygame.key.set_repeat(50, 25)
# pętla główna programu
while True:
	# obsługa zdarzeń generowanych przez gracza
	for event in pygame.event.get():
		# przechwyć zamknięcie okna
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		# przechwyć ruch myszy
		if event.type == MOUSEMOTION:
			myszaX, myszaY = event.pos # współrzędne x, y kursora myszy
			
			# oblicz przesunięcie paletki gracza
			przesuniecie = myszaX - (PALETKA_SZER / 2)
			
			# jeżeli wykraczamy poza okno gry w prawo
			if przesuniecie > OKNOGRY_SZER - PALETKA_SZER:
				przesuniecie = OKNOGRY_SZER - PALETKA_SZER
			# jeżeli wykraczamy poza okno gry w lewo
			if przesuniecie < 0:
				przesuniecie = 0
			# zaktualizuj położenie paletki w poziomie
			paletka1_prost.x = przesuniecie
		
		#przechwyć naciśnięcie klawiszy kursora
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				paletka1_prost.x -= 5
				if paletka1_prost.x < 0:
					paletka1_prost.x = 0
			if event.key == pygame.K_RIGHT:
				paletka1_prost.x += 5
				if paletka1_prost.x > OKNOGRY_SZER - PALETKA_SZER:
					paletka1_prost.x = OKNOGRY_SZER - PALETKA_SZER
	
	# ruch piłki #######################################################
	# przesuń piłkę po obsłudze zdarzeń
	pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)
	
	# jeżeli piłka wykracza poza pole gry
	# z lewej/prawej - odwracamy kierunek ruchu poziomego piłki
	if pilka_prost.right >= OKNOGRY_SZER:
		P_PREDKOSC_X *= -1
	if pilka_prost.left <= 0:
		P_PREDKOSC_X *= -1
	# góra/dół
	if pilka_prost.top <= 0:
		#P_PREDKOSC_Y *= -1
		pilka_prost.x, pilka_prost.y = OKNOGRY_SZER / 2, OKNOGRY_WYS / 2
		PKT_1 = str(int(PKT_1) + 1)
	if pilka_prost.bottom >= OKNOGRY_WYS:
		pilka_prost.x, pilka_prost.y = OKNOGRY_SZER / 2, OKNOGRY_WYS / 2
		PKT_AI = str(int(PKT_AI) + 1)
		
	# AI ###############################################################
	# jeżeli piłka ucieka na prawo, przesuń za nią paletkę
	if pilka_prost.centerx > paletkaAI_prost.centerx:
		paletkaAI_prost.x += PREDKOSC_AI
	# w przeciwnym wypadku przesuń w lewo
	elif pilka_prost.centerx < paletkaAI_prost.centerx:
		paletkaAI_prost.x -= PREDKOSC_AI
		
	# jeżeli piłka dotknie paletki AI, skieruj ją w przeciwną stronę
	if pilka_prost.colliderect(paletkaAI_prost):
		P_PREDKOSC_Y *= -1
		# uwzględnij nachodzenie paletki na piłkę (przysłonięcie)
		pilka_prost.top = paletkaAI_prost.bottom
		
	# jeżeli piłka dotknie paletki gracza, skieruj ją w przeciwną stronę
	if pilka_prost.colliderect(paletka1_prost):
		P_PREDKOSC_Y *= -1
		# zapobiegaj przysłanianiu paletki przez piłkę
		pilka_prost.bottom = paletka1_prost.top	
			
	# rysowanie obiektów
	oknogry.fill(LT_BLUE) # kolor okna gry
	
	# wyświetlanie punktacji
	drukuj_punkty(PKT_1, OKNOGRY_SZER / 2, OKNOGRY_WYS * 0.75, oknogry)
	drukuj_punkty(PKT_AI, OKNOGRY_SZER / 2, OKNOGRY_WYS / 4, oknogry)
	
	# narysuj w oknie gry paletki
	oknogry.blit(paletka1, paletka1_prost)
	oknogry.blit(paletkaAI, paletkaAI_prost)	
	
	# narysuj w oknie piłkę
	oknogry.blit(pilka, pilka_prost)
	
	# zaktualizuj okno i wyświetl
	pygame.display.update()
	
	# zaktualizuj zegar po narysowaniu obiektów
	fpsClock.tick(FPS)
	
# KONIEC
