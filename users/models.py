from django.db import models

class User(models.Model):
	login = models.CharField(max_length = 30)
	full_name = models.CharField(max_length = 30)
	date_birthday = models.DateField()

	def __unicode__(self):
		return '%s %s %s' % (self.login, self.full_name, self.date_birthday)