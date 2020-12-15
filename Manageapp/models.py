from django.db import models
import datetime

# Create your models here.
class Vendor(models.Model):
	name=models.TextField(max_length=50)
	contact=models.TextField()
	def __str__(self):
		return self.name

class Milkentry(models.Model):
	name=models.TextField(max_length=50)
	date = models.DateField(("Date"), default=datetime.date.today , blank=True ,null=False)
	milktype=models.TextField(default='none')
	quantity=models.FloatField(default=0.0)
	fat=models.FloatField(default=0.0)
	snf=models.FloatField(default=0.0)
	bill=models.FloatField(default=0.0)
	def __str__(self):
		return self.name