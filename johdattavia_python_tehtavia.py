#Johdattavia python tehtavia

#1.Tee funktio, joka tulostaa sanan kissa
def kissaprintti():
	print("kissa")

#2.Tee funktio, joka tulostaa sanan koira
def koiraprintti():
	print("koira")

#3.Tee funktio, joka yhdistää edelliset
def elainyhdistelmatulostaja():
	kissaprintti()
	koiraprintti()

#4.Tee funktio, joka tulostaa sanan "kissa" kymmenen kertaa
def tulostakissat():
	tulos = ""
	for x in range(10):
		tulos += "kissa "
	print(tulos)

#5.Muuta edellistä niin, että se käyttää funktiota elainyhdistelmatulostaja
def tulostakissat_2():
	for x in range(10):
		elainyhdistelmatulostaja()

#6.Tee funktio, joka tulostaa juoksevan numeronm ja sanan "kissa" 10 kertaa
def tulostanumerokissat():
	tulos = ""
	for x in range(10):
		tulos += f'{x+1} kissa '
	print(tulos)

#7.Tee funktio, joka tulostaa taulukon alkioita vuorotellen
def tulostavuorotellen(lista):
	tulos = ""
	for x in range(10):
		if x % 2 == 0:
			tulos += lista[0]+ " "
		else:
			tulos += lista[1]+ " "
	print(tulos)

#8.Tee ehto, joka printtaa "10", jos luku on suurempi kuin 10
def ehto():
	a = 23
	if a > 10:
		print("10")

#9.Tee funktio "kokeile", joka palauttaa luvun 10, jos sille annettu luku on suurempi kuin 10
def kokeile(num):
	if num > 10:
		return 10

#10.Tee funktio, joka tulostaa luvut 1-10
def tulostakymmenen():
	tulos = ""
	for x in range(1,11):
		tulos += str(x) + " "
	print(tulos)

#11.Tee funktio, joka tulostaa luvut 1-20 kahden välein
def tulosta20_jokatoinen():
	tulos = ""
	for x in range(1,21,2):
		tulos += str(x) + " "
	print(tulos)

#12.Lisää edelliseen ehto, joka tulostaa "suurempi kuin kymmenen"
def tulosta20_jokatoinen_ilmoitus():
	tulos = ""
	for x in range(1,21,2):
		if x > 10 and x <= 11:
			tulos += "suurempi kuin kymmenen "
		else:
			tulos += str(x) + " "
	print(tulos)


#13.Tee funktio, joka laskee annetun taulukon alkiot yhtee ja palauttaa summan
def summaakaikki(lista):
	total = 0
	for x in lista:
		total += x

	return total