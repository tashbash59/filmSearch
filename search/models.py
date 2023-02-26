from django.db import models

class SearchNumbers(models.Model):
	first = models.IntegerField()
	second = models.IntegerField()