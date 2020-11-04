

#Tuples
def pikku():
	a = 2
	b = 3
	return a,b,a+b, "kissa"

foo = pikku()

mun_a, mun_b, mun_summa, mun_kissa = foo

#Parametrikasa
def syssy(*muuttujat):
	for temparvo in muuttujat:
		print("Temparvo=", temparvo)

#lähes identtinen seuraavan kanssa
#syssy([1,2,3,4])

def roisto(eka, toka):
	print(eka)

#muokattu lista annetusta listasta
def listankasittely(munlista):
	tuloslista, tuloslista_2 = [], []
	
	for alkio in munlista:
		tuloslista.append(alkio+5)
		tuloslista_2.append(alkio*alkio)
	return tuloslista, tuloslista_2
print(listankasittely([1,2,3,4]))


