#requests -kirjasto täytyy asentaa, "pip install requests -> cmd"
import requests
import json

#Vitsi classi
class Vitsi:
	def __init__(self, id, joke):
		self.id = id
		self.joke = joke

#Hakee vitsit API
def get_jokes():
	url = "https://icanhazdadjoke.com/"
	res = requests.get(url, headers={"Accept":"application/json"})
	data = json.loads(res.text)
	return data

#Tekee listan Vitsi -olioita
def make_joke_list():
	jokes = []
	for x in range(20):
		vitsi = get_jokes()
		jokes.append(Vitsi(vitsi["id"], vitsi["joke"]))

	return jokes

#Tulostaa kaikki vitsit
def print_jokes():
	for x in make_joke_list():
		print(x.joke)

#Tekee annetun nimisen .txt tiedoston ja lisää vitsit
def tee_vitsi_tiedosto(filename):
	with open(f'{filename}.txt', "w") as file:
		for vitsi in make_joke_list():
			file.write(vitsi.joke+"\n")

tee_vitsi_tiedosto("vitsitiedosto")