from django.test import TestCase
from.models import Teacher

class TeacheartTestCase(TestCase):
	def setUp(self):
		self.teacher=Teacher(
	first_name="chess",
	last_name="Alexis",
	regestration_number='6688775698',
	place_of_resident="Kilimani",
	phone_number="0998876564",
	email="chesangfelister20@gmail.com",
	Id_number="8778967",
	date_joined='datetime.date.today()',
	profession="software dev",
			)

		
