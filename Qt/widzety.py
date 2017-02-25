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
			self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanal)
		self.suwak.valueChanged.connect(self.zmienKolor)
		# Lista ComboBox i SpinBox ###
		self.grupaRBtn.clicked.connect(self.ustawStan)
		self.listaRGB.activated[str].connect(self.ustawKanal)
		self.spinRGB.valueChanged[int].connect(self.zmienKolor)
		# przyciski PushButton ###
		for btn in self.grupaP.buttons():
			btn.clicked[bool].connect(self.ustawKanalPBtn)
		self.grupaPBtn.clicked.connect(self.ustawStan)
		# etykiety QLabel i pola QEditLine ###
		for v in ('R', 'G', 'B'):
			kolor = getattr(self, 'kolor' + v)
			kolor.textEdited.connect(self.zmienKolor)
		#self.info()
			
			
	def info(self):
		fontB = "QWidget { font-weight: bold }"
		fontN = "QWidget { font-weight: normal }"
		
		for v in ('R', 'G', 'B'):
			label = getattr(self, 'label' + v)
			kolor = getattr(self, 'kolor' + v)
			if v in self.kanaly:
				label.setStyleSheet(fontB)
				kolor.setEnabled(True)
			else:
				label.setStyleSheet(fontN)
				kolor.setEnabled(False)
		'''		
		self.kolorR.setText(str(self.kolorW.red()))
		self.kolorG.setText(str(self.kolorW.green()))
		self.kolorB.setText(str(self.kolorW.blue()))
		'''
		
	def ustawStan(self, wartosc):
		nadawca = self.sender()
		#self.kanaly = set()
		if wartosc:
			self.listaRGB.setEnabled(False)
			self.spinRGB.setEnabled(False)
			if nadawca == self.grupaPBtn:
				self.grupaRBtn.setChecked(False)
				self.kanaly = set()
				for i in range(self.ukladP.count()):
					if self.ukladP.itemAt(i).widget().isChecked():
						kanal = self.ukladP.itemAt(i).widget().text()
						self.kanaly.add(kanal)
			elif nadawca == self.grupaRBtn:
				self.grupaPBtn.setChecked(False)
				self.kanaly = set()
				for i in range(self.ukladR.count()):
					if self.ukladR.itemAt(i).widget().isChecked():
						kanal = self.ukladR.itemAt(i).widget().text()
						self.kanaly.add(kanal)
		else:
			self.listaRGB.setEnabled(True)
			self.spinRGB.setEnabled(True)
			self.kanaly = set()
			self.kanaly.add(self.listaRGB.currentText())
		self.info()
			
			
	def ustawKanalPBtn(self, wartosc):
		nadawca = self.sender()
		if wartosc:
			self.kanaly.add(nadawca.text())
		elif nadawca.text() in self.kanaly:
			self.kanaly.remove(nadawca.text())
		self.info()
			
			
	def ustawKanalCBox(self, wartosc):
		self.kanaly = set() # resetujemy zbiór kanałów
		self.kanaly.add(wartosc)
		self.info()
		
		
	def ustawKanalRBtn(self, wartosc):
		self.kanaly = set() # resetujemy zbiór kanałów
		nadawca = self.sender()
		if wartosc:
			self.kanaly.add(nadawca.text())
		self.info()
		
		
	def ustawKanal(self, wartosc):
		self.kanaly = set()
		nadawca = self.sender()
		if type(wartosc) == str:
			self.kanaly.add(wartosc)
		elif type(wartosc) == bool:
			if wartosc:
				self.kanaly.add(nadawca.text())
		self.info()
					
			
	def zmienKolor(self, wartosc):
		try:
			wartosc = int(wartosc)
		except ValueError:
			wartosc = 0
		if wartosc > 255:
			wartosc = 255
			
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
		#self.info()
		# napisy w polach LineEdit
		self.kolorR.setText(str(self.kolorW.red()))
		self.kolorG.setText(str(self.kolorW.green()))
		self.kolorB.setText(str(self.kolorW.blue()))
		
		
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
