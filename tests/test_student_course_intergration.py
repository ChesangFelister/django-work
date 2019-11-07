from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime


class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a=Student.objects.create(
			first_name='chesang',
			last_name='Alexis',
			date_of_birth=datetime.date(2000,8,13),
			regestration_number='662387876',
			place_of_resident='ghggfg',
			email="chesangfelister@gmail.com",
			phone_number='07345442323',
			guardian_phone_number='09878654',
			Id_number='001',
			date_joined=datetime.date.today(),
			
	
			)
		self.course_b=Course.objects.create(
			name="python",
            duration_in_months="4",
            course_number="667765",
            description="data",

			)
		self.teacher_c=Teacher.objects.create(
			first_name="lucy",
			last_name="Njeri",
			regestration_number="6677865",
			place_of_resident="Nairobi",
			phone_number="076533323",
			email="chesangfelister@gmail.com",
			Id_number="987768787",
			date_joined=datetime.date.today(),
			profession="Developer"
	)
		self.python =Course.objects.create(
			name="python",
            duration_in_months="5",
            description="the use solving data to provide solution",
			)
		self.javascript =Course.objects.create(
			name="Javascript",
            duration_in_months="6",
            description="creating fast and impressive website to people",
			)

		self.hardware =Course.objects.create(
			name="hardware",
            duration_in_months="4",
            description="creating and designing different",
			)
		self.teacher =Teacher.objects.create(
			first_name="jenny",
			last_name="chepkopus",
			regestration_number="66005",
			place_of_resident="Nairobi",
			phone_number="07777999",
			email="chesangfelister20@gmail.com",
			Id_number="987768787",
			date_joined=datetime.date.today(),
			profession="Designer"
			)
	def test_student_can_join_many_courses(self):
		self.assertEqual(self.student_a.courses.count(),0)
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.javascript)
		self.assertEqual(self.student_a.courses.count(),2)
		self.student_a.courses.add(self.hardware)
		self.assertEqual(self.student_a.courses.count(),3)

	def test_course_can_have_many_students(self):
		self.python.student.add(self.student,self.student_b)
		self.assertEqual(self.python.students.count(),2)




# class StudentCourseTeacherTestCase(self):
	
 











	# def test_course_can_join_only_one_teacher(self):
	# 	self.assertEqual(self.teacher.courses.count(),0)
	# 	self.course_b.courses.add(self.python)
	# 	self.assertEqual(self.teacher.courses.count(),1)