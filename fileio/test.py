
ladatturuokalista = ["Leipa", "1", "2", "Pulla", "3", "5", "Leipa", "4", "5"]

class Leipomotuotteet:
	def __init__(self):
		self.tyyppi = "ei_tiedeta"
		self.maara = 0
		self.hinta = 0

#tayta lista Leivat luokan olioilla
#kuinka?

leivat_olioina = []

for x in range(0, len(ladatturuokalista), 3):
	o = Leipomotuotteet()
	o.tyyppi = ladatturuokalista[x]
	o.maara = ladatturuokalista[x+1]
	o.hinta = ladatturuokalista[x+2]
	leivat_olioina.append(o)


for y in leivat_olioina:
	print(f'tyyppi: {y.tyyppi}, maara: {y.maara}, hinta: {y.hinta}')	