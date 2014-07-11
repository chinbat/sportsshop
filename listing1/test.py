from django.test import TestCase
from listing1.models import Category1

class Post1TestCase(TestCase):
	def createCategory(self):
		Post1.objects.create(name="")
