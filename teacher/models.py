from django.db import models


# Create your models here.
class Teacher(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	regestration_number=models.CharField(max_length=50)
	place_of_resident=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	Id_number=models.IntegerField()
	date_joined=models.DateField(max_length=50)
	profession=models.CharField(max_length=50)
	image=models.FileField(upload_to="profile_image",blank=True,null=True)
	def __str__(self):
		return self.first_name+" "+self.last_name