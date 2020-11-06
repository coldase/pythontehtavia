#PYTHON ALKUHARJOITUKSIA 2

#Parametrit

#1.
def palauta(*args):
	return args

#2.
def palauta_sum(*args):
	total = 0
	for x in args:
		total += x
	return total

#3.
def toimi(suunta):
	print(f'Hissi on menossa {suunta}')

#4.
def kaanna(*args):
	return tuple(args[::-1])

#5.
def kaanna_2(*args):
	return list(args[::-1])

#6.
def tee_tauluksi(tup):
	taulukko = []
	for x in tup:
		taulukko.append(x)
	return taulukko


#Ehdot

#7.
def yhtasuuret(a,b):
	if a == b:
		return "Tosi"

#8.
def yhtasuuret_2(a,b,c):
	if a == b and a > c:
		return "Tosi"

#9.
def testaa(lista, sana):
	return sana in lista

#10
def testaa_2(lista, sana):
	lippu = 0
	if lippu == 0:
		print("Tosi")
	for x in lista:
		if x == sana:
			lippu = 1

#11.
def testaa_3(a,b,c,d):
	if d == "TESTI":
		if a == b and a > c and b > c:
			return True

#12.
def testaa_4(a,b):
	return a != b

#13.
def aputulostus():
	print("Ovat erisuuria!")

def testaa_5(a,b):
	if a != b:
		aputulostus()



#Taulukot

#14.
def yhdistelma(a,b):
	result = []
	for x in a:
		result.append(x)
	for x in b:
		result.append(x)
	return result


#Bonus

#15.
oksat = [0,1,0,1,2,2,0,1,0,1]
atomi =["a","b","c"]
def puurakenne(ok, at):
	result = []
	for x in ok:
		result.append(at[x])

	return result

#16.
def testaaja(a):
	if a == 5:
		print("Liian pieni")
		return -999

def funk(a,b):
	if a != b:
		testaaja(a)