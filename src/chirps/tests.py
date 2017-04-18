from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from .models import Chirp

User = get_user_model()

class Test(TestCase):
	def setUp(self):
        	some_random_user = User.objects.create(username='jmitchel33333333333')

	def Test_Chirp(self):
		obj = Chirp.objects.create(user= User.objects.first(), content='Some Random Content')
		self.assertTrue(obj.content == "Some random content")
        self.assertTrue(obj.id == 1)
        #self.assertEqual(obj.id, 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
