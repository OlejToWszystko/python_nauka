#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os, json


def ustawienia():
    """Funkcja pobiera nick, ilość losowanych liczb, maksymalną losowaną
	wartość oraz ilość prób. Pozwala określić stopień trudności gry.
	Ustawienia są zapisywane w pliku"""

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawienia:")
        print("Liczb:", gracz[1])
        print("Z Maks:", gracz[2])
        print("Losowań:", gracz[3])
        odp = input("Zmieniasz (t/n)?")

    if not gracz or odp.lower() == "t":
        while 1:
            try:
                ile = int(input("Podaj ilość typowanych liczb: "))
                maks = int(input("Podaj maksymalną losowaną liczbę: "))
                if ile > maks:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except:
                print("Błędne dane!")
                continue
        gracz = zapisz_ust(nazwapliku, [nick, str(ile), str(maks), str(ilelos)])

    return gracz[0:1] + list(map(lambda x: int(x), gracz[1:4]))


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()
    return gracz


def losujliczby(ile, maks):
    # Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby


def pobierztypy(ile, maks):
    # Funkcja pobiera od użytkownika jego typy wylosowanych liczb
    print("Wytypuj", ile, "z", maks, " liczb")
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbę " + str(i + 1) + ": "))
        except ValueError:
            print("Błędne dane!")
            continue

        if 0 < typ <= maks and typ not in typy:
            typy.add(typ)
            i = i + 1
    return typy


def wyniki(typy, liczby):
    '''Funkcja pobiera zbiór typów i listę liczb, wyznacza iloczyn
	zbiorów i podaje ilość elementów wspólnych'''
    trafione = set(liczby) & typy

    if trafione:
        print("\nIlość trafień:", len(trafione))
        print("Trafione liczby to :", str(trafione).strip('[]'))
    else:
        print("Brak trafień")

    print("\n" + "x" * 40 + "\n")
    return len(trafione)

def czytaj_json(nazwapliku):
	#Funkcja odczytuje dane w formacie json z pliku
	dane = []
	if os.path.isfile(nazwapliku):
		with open(nazwapliku, "r") as plik:
			dane = json.load(plik)
	return dane

def zapisz_json(nazwapliku, dane):
	#Funkcja zapisuje dane w formacie json do pliku
	with open(nazwapliku, "w") as plik:
		json.dump(dane, plik)

def czytaj_str(nazwapliku):
	#Funkcja odczytuje dane w formacie txt z pliku
	dane = []
	slownik = {}
	if os.path.isfile(nazwapliku):
		with open(nazwapliku, "r") as plik:
			linie = plik.readlines() 
			for linia in linie:
				linia = linia.strip() #usuwa białe znaki
				wers = linia.split(";")
				for i in wers:
					slownik.update([i.split(":")])
				dane.append(slownik)
				slownik = {}
	return dane

def zapisz_str(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie txt do pliku"""
    with open(nazwapliku, "w") as plik:
        for slownik in dane:
            linia = [k + ":" + str(w) for k, w in slownik.items()]
            linia = ";".join(linia)
            # plik.write(linia+"\n") – zamiast tak, można:
            #print >>plik, linia
            print(linia, file=plik)
