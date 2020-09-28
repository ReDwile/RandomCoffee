class UserData:
	def __init__(self):
		self.name = str()     # real name of the user
		self.surname = str()  # real surname of the user
		self.age = int()      # age of the user

		self.tgUserName = str()  # telegram user name
		self.tgUserID = int()    # telegram user id

		self.socialNetworkLinks = list()  # list of links to social network pages of the user
		self.phoneNumber = str()          # phone number of the user

		self.relevant = bool()       # Is user active
		self.participation = bool()  # Will user participate in the next meeting
