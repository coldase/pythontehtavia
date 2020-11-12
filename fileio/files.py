#Oma tiedostomuoto: ruokakauppalista, jatke = kpl

import random

tuotteet = ["omena", "kahvi", "maito", "sipuli", "perunat"]


def kirjoittaja():
	with open("kauppalista.kpl", "w") as file:
		file.write("#kauppalista\n#tuote, maara, hinta, alennus%\n#\n")
		for x in range(100):
			maara = random.randint(0, 100)
			alennus = random.randint(0, 100)
			tuote = random.choice(tuotteet)
			hinta = random.randint(1, 1000)
			file.write(f"{tuote} {maara} {hinta} {alennus} %\n")


def tee_oliot(filename):
	with open(filename, "r") as file:
		content = file.readlines()
		oliolista = []
		new = []
		for items in content:
			if items[0] != "#":
				new.append(items)

		for y in new:
			tuote, maara, hinta, alennus, *rest = y.split()
			oliolista.append(Ruoka(tuote, maara, hinta, alennus))			

		return oliolista

class Ruoka:
	def __init__(self, tuote, maara, hinta, alennus):
		self.tuote = tuote
		self.maara = maara
		self.hinta = hinta
		self.alennus = alennus



# kirjoittaja()

#poista kommenttirivit
#poista merkit
#tulosta 
#splittaa taulukoksi

#tee tuotteista oliot
# "class Ruoka:"
#		self.tuote
#		self.hinta
#		self.maara
#		self.alennus

#lisää oliot listaan