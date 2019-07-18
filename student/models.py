from django.db import models
from course.models import Course

# Create your models here.
class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	regestration_number=models.CharField(max_length=50) 
	place_of_resident=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	guardian_phone_number=models.CharField(max_length=50)
	Id_number=models.IntegerField()
	date_joined=models.DateField(max_length=50)
	courses=models.ManyToManyField(Course)
	image=models.ImageField(upload_to="profile_image",blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name
