from django.db import models

class Content(models.Model):
	title = models.CharField(max_length = 500)
	subtitle = models.CharField(max_length = 500)
	contributors = models.ManyToManyField('Contributor', null = True, related_name = 'content')
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title

class Article(Content):
	text = models.CharField(max_length = 1000)

class Image(Content):
	path = models.FilePathField(path = '/home/Dropbox/CrimComp/Assignments/3')

	def info(self):
		return '{0}\n{1}\npath: {2}'.format(self.title, self.subtitle, self.path)

class Contributor(models.Model):
	first_name = models.CharField(max_length = 500)
	last_name = models.CharField(max_length = 500)

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)

	def die(self):
		for c in self.contents:
			c.contributors.remove(self)
		self.delete()

