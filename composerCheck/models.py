from django.db import models

# Create your models here.

class Vulnerability(models.Model):
	description = models.CharField(max_length = 400)
	package = models.CharField(max_length = 400)
	version = models.CharField(max_length = 20) # TODO: this should be something like a float
# This should be in phishtank	ip_address = models.IntegerField(default=0)
	def __unicode__(self):
		return self.description
