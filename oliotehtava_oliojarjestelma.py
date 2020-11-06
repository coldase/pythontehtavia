

class Facebook:
	def __init__(self):
		self.users = []


	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.pop(user)

	def show_users(self):
		print(self.users)


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
		print(app.users)

app = Facebook()

markku = User("Markku")
kalle = User("Kalle")

markku.send_message(kalle, "moro")
