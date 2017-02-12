#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  widzety.py

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor
from gui import Ui_Widget


class Widgety(QWidget, Ui_Widget):
	""" Głównka klasa aplikacji """
	
	kanaly = {'R'} # zbiór kanałów
	kolorW = QColor(0, 0, 0) # kolor RGB kształtu 1
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self) # tworzenie interfejsu
		
		# Sygnały i sloty
		# przyciski CheckBox 
		self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
		self.ksztaltChk.clicked.connect(self.aktywujKsztalt)
		# Slider + przyciski RadioButton 
		for i in range(self.ukladR.count()):
			self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanalRBtn)
		self.suwak.valueChanged.connect(self.zmienKolor)
		
		
	def ustawKanalRBtn(self, wartosc):
		self.kanaly = set() # resetujemy zbiór kanałów
		nadawca = self.sender()
		if wartosc:
			self.kanaly.add(nadawca.text())
			
			
	def zmienKolor(self, wartosc):
		self.lcd.display(wartosc)
		if 'R' in self.kanaly:
			self.kolorW.setRed(wartosc)
		if 'G' in self.kanaly:
			self.kolorW.setGreen(wartosc)
		if 'B' in self.kanaly:
			self.kolorW.setBlue(wartosc)
			
		self.ksztaltAktywny.ustawKolorW(
			self.kolorW.red(),
			self.kolorW.green(),
			self.kolorW.blue())
		
		
	def ustawKsztalt(self, wartosc):
		self.ksztaltAktywny.ustawKsztalt(wartosc)
		
		
	def aktywujKsztalt(self, wartosc):
		nadawca = self.sender()
		if wartosc:
			self.ksztaltAktywny = self.ksztalt1
			nadawca.setText('<=')
		else:
			self.ksztaltAktywny = self.ksztalt2
			nadawca.setText('=>')
		self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()
    
    sys.exit(app.exec_())
