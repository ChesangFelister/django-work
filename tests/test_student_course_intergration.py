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
		self.student_b=Student.objects.create(
			first_name='lucy',
			last_name='kamoyu',
			date_of_birth=datetime.date(2000,8,13),
			regestration_number='6623890',
			place_of_resident='ghggfg',
			email="chesangfelister@gmail.com",
			phone_number='089076744',
			guardian_phone_number='0980084',
			Id_number='002',
			date_joined=datetime.date.today(),
			
	
			)
		self.course_b=Course.objects.create(
			name="python",
            duration_in_months="4",
            course_number="667765",
            description="data",

			)
		self.teacher_c=Teacher.objects.create(
			first_name="James",
			last_name="Mwai",
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
			first_name="Jenny",
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
		self.python.student.add(self.student_a,self.student_b)
		self.assertEqual(self.python.student.count(),2)

	def test_teacher_can_have_many_courses(self):
		self.javascript.teacher = self.teacher
		self.hardware.teacher = self.teacher
		self.assertEqual(self.javascript.teacher,self.hardware.teacher)

		

	def test_course_can_not_have_many_teachers(self):
		self.python.teacher = self.teacher
		self.assertEqual(self.python.teacher.first_name,"Jenny")
		self.python.teacher = self.teacher_c
		self.assertEqual(self.python.teacher.first_name,"James")
	
	def test_course_teacher_is_in_student_teachers_list(self):
		self.javascript.teacher = self.teacher
		self.student_a.courses.add(self.python)
		teacher=self.student_a.teacher()
		self.assertTrue(self.teacher in teacher)

























# def test_course_cannot_have_many_teachers(self):
# 		self.python.teacher = self.teacher_a
# 		self.python.teacher = self.teacher_b
# 		self.assertTrue(self.python.teacher==self.teacher_a)




# def test_teacher_can_not_have_many_courses(self):
	# 	self.python.teacher.add(self.python)
	# 	self.assertFalse(self.python.teacher.count(),2)
# class StudentCourseTeacherTestCase(self):



	# def test_course_can_join_only_one_teacher(self):
	# 	self.assertEqual(self.teacher.courses.count(),0)
	# 	self.course_b.courses.add(self.python)
	# 	self.assertEqual(self.teacher.courses.count(),1)