from datetime import date

class Content(object):
	# list to keep track of all pieces of content
	existing_content = []

	def __init__(self, year, month, day, contributors):
		# log each piece of content as existing upon creation
		existing_content.append(self)

		# TODO: store year, month, day (hint: check out datetime.date)
		

		# list of contirbutors
		self.contributors = contributors

	# this defines a show method that has nothing in it, to be overridden later
	def show(self):
		raise NotImplementedError


# TODO: Define an Article class that extends the Content class


# TODO: Define a Picture class that extends the Content class
