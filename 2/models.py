from datetime import date
from PIL import Image

class Content(object):
	# list to keep track of all pieces of content
	existing_content = []

	def __init__(self, year, month, day, contributors):
		# log each piece of content as existing upon creation
		self.existing_content.append(self)

		# store year, month, day (hint: check out datetime.date)
		self.creation_date = date(year, month, day)

		# list of contirbutors
		self.contributors = contributors

	# this defines a show method that has nothing in it, to be overridden later
	def show(self):
		raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):
	def __init__(self, year, month, day, headline, content, contributors):
		# initializes Content attributes
		Content.__init__(self, year, month, day, contributors)

		# stores headline and content
		self.headline = headline
		self.content = content

	# defines show method that prints to terminal in pretty way
	def show(self):
		print self.headline
		print self.contributors
		print self.creation_date
		print self.content

# TODO: Define a Picture class that extends the Content class
class Picture(Content):
	def __init__(self, year, month, day, title, caption, path, contributors):
		# initializes Content attributes
		Content.__init__(self, year, month, day, contributors)

		# initializes picture specific attributes
		self.title = title
		self.caption = caption
		self.path = path

	# defines show method that prints info in pretty way
	def show(self):
		print self.title
		print self.contributors
		print self.creation_date
		print self.caption
		print self.path
		im = Image.open(self.path)
		im.load()


