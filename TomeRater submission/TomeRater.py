class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}			# Book object:users rating

	def get_email(self):
		return self.email

	def change_email(self, updated_email):
		self.email = updated_email
		return "The users e-mail has now been updated to " + self.email

	def __repr__(self):
		return "user: {}, e-mail: {}, No. of books read: {}".format(self.name, self.email, len(self.books))

	def __eq__(self, other_user):
		return self.name == other_user.name and self.email == other_user.email
			
	def read_book(self, book, rating = None):
		if rating != None:
			self.books[book] = rating
		return self.books

	def get_average_rating(self):
		total_rating = 0
		for rating in self.books.values():
			total_rating += rating
		return total_rating/len(self.books)

class Book:
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, updated_isbn):
		self.isbn = updated_isbn
		return "{}'s ISBN has been updated to {}".format(self.title, self.isbn)

	def add_rating(self, rating):
		if rating >= 0 and rating <= 4:
			self.ratings.append(rating)
			return self.ratings
		else:
			return "Invalid rating"

	def __eq__(self, other_book):
		return self.title == other_book.title and self.isbn == other_book.isbn
	
	def get_average_rating(self):
		total_rating = 0
		for rating in self.ratings:
			total_rating += rating
		if len(self.ratings) > 0:
			return total_rating/len(self.ratings)
		else:
			return 0
    
	def __hash__(self):
		return hash((self.title, self.isbn))

	def __repr__(self):
		return "{}".format(self.title)
  
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)  
		self.author = author

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)  
		self.subject = subject
		self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater:
	def __init__(self):
		self.users = {}		# takes email and User object
		self.books = {} 	# takes Book object and no. of Users that have read it
		
	def create_book(self, title, isbn):
		return Book(title, isbn) 

	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)

	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn)

	def add_book_to_user(self, book, email, rating = None):
		if email in self.users:
			new_user = self.users.get(email, "No user with e-mail {email}!")
			new_user.read_book(book, rating)
			if book in self.books:
				self.books[book] += 1
				book.add_rating(rating)
			else:
				self.books[book] = 1  
		else:
			return "No user with e-mail {email}!"
  
	def add_user(self, name, email, user_books = None):
		self.users[email] = User(name, email)
		if user_books != None:
			for book in user_books:
				self.add_book_to_user(book, email) 
			      
	def print_catalog(self): 
		print("Catalog list: ")
		for book in self.books.keys():
			print(book)

	def print_users(self):
		print("User list: ")
		for user in self.users.keys():
			print(user)

	def most_read_book(self):
		most_read= 0
		most_read_book = ""
		for book, count in self.books.items():
			if count > most_read:
				most_read = count
				most_read_book = book
		return "'{}' is the most read book by {} users".format(most_read_book, most_read)

	def highest_rated_book(self):
		highest_rated_book = ""
		highest_average_book_rating = 0
		for book in self.books.keys():
			if book.get_average_rating() > 0:
				highest_average_book_rating = book.get_average_rating()
				highest_rated_book = book
		return "Highest rated book is '{}' with a rating of {}".format(highest_rated_book, highest_average_book_rating)

	def most_positive_user(self):
		most_positive_user = ""
		highest_average_user_rating = 0
		for user in self.users.values():
			if user.get_average_rating() > highest_average_user_rating:
				most_positive_user = user
				highest_average_user_rating = user.get_average_rating()
		return "Most positive {} with an average rating of {}".format(most_positive_user, highest_average_user_rating)