from django.db import models
from course.models import Course
from django.core.exceptions import ValidationError
from teacher.models import Teacher

import datetime
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
	courses=models.ManyToManyField(Course,related_name="student",blank=False)
	image=models.ImageField(upload_to="profile_image",blank=True,null=True)

	def __str__(self):
		return self.first_name+" "+self.last_name

	def full_name(self):
		return "{} {}".format(self.first_name,self.last_name)

	def get_age(self):
		today = datetime.date.today()
		return today.year - self.date_of_birth.year
	age = property(get_age)
	def clean(self):
		age = self.age
		if age <18 or age>30:
			raise ValidationError("Only above 17 years and Above 30 years")
		return age

	def teachers(self):
		return[courses.teacher for courses in self.courses.all]
