from django.db import models

class FakeData(models.Model):
	id=models.IntegerField(primary_key=True)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	job=models.CharField(max_length=30)
	salary=models.IntegerField()
	city=models.CharField(max_length=30)
