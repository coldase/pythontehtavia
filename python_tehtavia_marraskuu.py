###################
# Funktiotehtavia #
###################

#1.Etsi pienempi
def pienempi(a,b):
	if a < b:
		return a
	return b

#2.Etsi suurempi
def suurempi(a,b):
	if a > b:
		return a
	return b

#3.Onko toinen luku x...
def paljonisompi(a,b,x):
	if a+x > b:
		return 0
	return 1

#4.Tee funktio, joka palauttaa löydetyn alkion naapurit
def palautanaapurit(li, alkio):
	i = 0
	for x in li:
		if x == alkio:
			return li[i-1], li[i+1]
		i += 1


###################
# Talukkotehtavia #
###################

#5.Sama ja naapurit
def sama_naap(li, alkio, raja):
	i = 0
	for x in li:
		if x == alkio:
			return li[i-raja:i+raja+1]
		i += 1

#1.Palauta joka toinen
def jokatoinen(li):
	return li[0::2]

#2.Tee funktio, joka tuottaa kaksi taulukkoa...
def erottele(li):
	parilliset, parittomat = [], []
	for x in li:
		if x % 2 == 0:
			parilliset.append(x)
		else:
			parittomat.append(x)
	return parilliset, parittomat

#3.Tee funktio, joka poistaa taulukosta alkion
def poista_alkio(li, alkio):
	newli = []
	for x in li:
		if x != alkio:
			newli.append(x)
	return newli

#4.Tee funktio, joka poistaa annetusta taulukosta..
def poista_alkiot(li_a, li_b):
	newli = []
	for x in li_a:
		if x not in li_b:
			newli.append(x)
	return newli

#5.Tee funktio, joka kääntää taulukon

#a) and b)
def kaanna(thingy):
	return thingy[::-1]

#c)
def interactive():
	word = input("Anna data: ")
	return word[::-1]

#6.Tee funktio, joka etsii taulukosta pienimmän arvon
def etsi_pienin(li):
	new = 0
	for x in li:
		if not new:
			new = x
		if x < new:
			new = x
	return new

#7.Tee functio, joka etsii taulukosta suurimman arvon
def etsi_suurin(li):
	new = 0
	for x in li:
		if not new:
			new = x
		if x > new:
			new = x
	return new

#8.Tee funktio, joka palauttaa taulukon keskiarvon
def keskiarvo(li):
	tulos = 0
	for x in li:
		tulos += x
	return int(tulos/len(li))

#9.Tee funktio, joka summaa yhteen kahden taulukon alkiot
def summaa(li_a, li_b):
	new = []
	for x in range(len(li_a)):
		new.append(li_a[x] + li_b[x])
	return new

#10.Tee funktio, joka summaa yhteen kahden erimittaisen...
def summaa_erimittaiset(li_a, li_b):
	new = []
	lyhyt = None
	if len(li_a) < len(li_b):
		lyhyt = li_a
	else:
		lyhyt = li_b

	for x in range(len(lyhyt)):
		new.append(li_a[x] + li_b[x])
	return new

#11.Tee funktio, joka yhdistää kahden erimittaisen...
def yhdista(li_a, li_b):
	lyhyt = li_b
	new = []
	if len(li_a) < len(li_b):
		lyhyt = li_a
	
	for x in range(len(lyhyt)):
		new.append(li_a[x])
		new.append(li_b[x])

	return new


###########################
# Moniulotteiset taulukot #
###########################

#12.Litistäminen
def litista(*args):
	new = []
	for x in args:
		for y in x:
			new.append(y)
	return new

#13.Tee kertotaulufunktio niin, että tuloksena on kaksiulotteinen...
def kertotaulutaulukossa():
	li = []
	for x in range(1,11):
		l = []
		for y in range(1,11):
			l.append(x*y)
		li.append(l)
	return li


################
# Oliotehtäviä #
################

#tein funktionin sisään, jotta ei tuu erroria kun koitan muita tehtäviä
#14.Määrittele olioluokka
def oliotehtava():

	class Auto:
		def __init__(self, tunniste):
			self.tunniste = tunniste

	autot = []
	for x in range(1,11):
		autot.append(Auto(x))

	for auto in autot:
		print(f'{auto} - Tunniste: {auto.tunniste}')


####################
# Nimigeneraattori #
####################

def nimigeneraattori():
	import string
	from random import choice
	a = ["a", "e", "i", "o", "u", "y"]
	b = [x for x in string.ascii_lowercase if x not in a]
	eka_tavu = [choice(a), choice(b), choice(a)]
	toka_tavu = [choice(b), choice(a)]
	name = eka_tavu + toka_tavu
	result = ""
	for x in name:
		result+=x
	return result


#################################
# Tiedostojen kirjoitus ja luku #
#################################

#16.Kirjoita taulukon sisältö tekstitiedostoon
def kirjoitatiedostoon(li, fi): #list, file
	with open(fi, "a") as file:
		for x in li:
			file.write(x+"\n")

#17.Lue tyhjään taulukkoon arvot tekstitiedostosta
def taytataulu(li, fi): #list, file
	with open(fi, "r") as file:
		for x in file.read().splitlines():
			li.append(x)
	return li