from django.test import TestCase
from.models import Student
import datetime
from.forms import StudentForm
from django.urls import reverse
from django.test import Client
from django.http import HttpResponseBadRequest
client=Client()


# Create your tests here.
class StudentTestCase(TestCase):
	def setUp(self):
		self.student=Student(
			first_name='chesang',
			last_name='Alexis',
			date_of_birth=datetime.date(2000,8,13),
			regestration_number='662387876',
			place_of_resident='ghggfg',
			email="chesangfelister@gmail.com",
			phone_number='07345442323',
			guardian_phone_number='09878654',
			Id_number='765456',
			date_joined=datetime.date.today(),
)

	def test_full_name_contain_first_name(self):
		self.assertIn(self.student.first_name,
			self.student.full_name())

	def test_full_name_contain_last_name(self):
		self.assertIn(self.student.last_name,self.student.full_name())

	def test_age_is_always_above_18(self):
		self.assertFalse(self.student.clean() <18)
	def test_age_is_always_below_30(self):
   		self.assertFalse(self.student.clean() >30)

class CreateStudentTestCase(TestCase):
	def setUp(self):
		self.data={
		"first_name":'chesang',
		"last_name":'Alexis',
		"date_of_birth":datetime.date(2000,8,13),
		"regestration_number":'662387876',
		"place_of_resident":'ghggfg',
		"email":"chesangfelister@gmail.com",
		"phone_number":'07345442323',
		"guardian_phone_number":'09878654',
		"Id_number":'765456',
		"date_joined":datetime.date(2010,8,13)
		}
		self.bad_data={
		"first_name":'888',
		"last_name":'67',
		"date_of_birth":datetime.date(2000,8,13),
		"regestration_number":'662387876',
		"place_of_resident":'ghggfg',
		"email":"",
		"phone_number":'0987654',
		"guardian_phone_number":'09878654',
		"Id_number":'765456',
		"date_joined":datetime.date(2010,8,13)}

	
	def test_student_form_always_valid_data(self):
		form=StudentForm(self.data)
		self.assertFalse(form.is_valid())

		
	def test_bad_student_form_reject_invalid_data(self):
		form=StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_student_view(self):
		url=reverse("add_student")
		request=client.post(url,self.data)
		self.assertEqual(request.status_code,400)

	def test_add_student_view_bad_data(self):
		url=reverse("add_student")
		request=client.post(url,self.bad_data)
		self.assertEqual(request.status_code,400)


	
	