
#Funktiotehtavia

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

#4.Tee funktio, joka palauttaa löydetyn...
def palautanaapurit(li, alkio):
	for x in li:
		if x == alkio:
			try:
				return li[x-1], li[x+1]
			except:
				pass
print(palautanaapurit([2,3,4], 3)) 



#Talukkotehtavia

####KESKEN####
#5.Sama ja naapurit
def sama_naap(li, x, raja):
	return 

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
	new = []
	for x in li:
		if not new:
			new.append(x)
		if x < new[0]:
			new[0] = x
	return new

#7.Tee functio, joka etsii taulukosta suurimman arvon
def etsi_suurin(li):
	new = []
	for x in li:
		if not new:
			new.append(x)
		if x > new[0]:
			new[0] = x
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
	lyhyt = None
	if len(li_a):
		tulos = []
		for x in li_a:
			tulos.append(x)
		for y in li_b:
			tulos.append(y)
		return tulos

# print(yhdista([2,3,4], [10,20,30,50]))
