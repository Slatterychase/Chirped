from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.


class Chirp(models.Model):
	#user
	user	= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content = models.CharField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})


	#def clean(self, *args, **kwargs):
		#content = self.content
		#if content == "abc":
		#	raise ValidationError("Cannot be ABC")
		#return super(Chirp, self).clean(*args, **kwargs)


