
class Facebook:
	def __init__(self):
		self.users = []

	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.pop(user)

	def show_users(self):
		print(self.users)

	#Anna seurattava user, printtaa kaverilistan ja viestit
	def seuraaja(self, user):
		print("FRIENDSLIST\n")
		for x in user.friends:
			print(f'- {x.username}')
		print("\nMESSAGES\n")
		for x in user.messages:
			print(x)
			
class User:
	def __init__(self, username):
		self.username = username
		self.friends = []
		self.messages = []
		app.add_user(self)

	def add_friend(self, friend):
		self.friends.append(friend)

	def remove_friend(self, friend):
		self.friends.pop(friend)

	def send_message(self, to, message):
		to.messages.append(message)


class Message:
	def __init__(self, actual_text):
		self.actual_text = actual_text

	def show_text(self):
		return self.actual_text


app = Facebook()

markku = User("Markku")
kalle = User("Kalle")
maija = User("Maija")

markku.send_message(kalle, Message("hei olen markku"))
maija.send_message(kalle, Message("moro, oon maija"))
kalle.add_friend(markku)
app.seuraaja(kalle)