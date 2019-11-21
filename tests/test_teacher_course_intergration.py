# from django.test import TestCase
# from student.models import Student
# from course.models import Course
# from teacher.models import Teacher
# import datetime
# class TeachersCourseTestCase(TestCase):
#     def setUP(self):
#         self.teacher_a = Teacher.objects.create(
#            first_name="lucy",
# 			last_name="Njeri",
# 			regestration_number="6677865",
# 			place_of_resident="Nairobi",
# 			phone_number="076533323",
# 			email="chesangfelister@gmail.com",
# 			Id_number="987768787",
# 			date_joined=datetime.date.today(),
# 			profession="Developer"
#            )
#         self.teacher_b = Teacher.objects.create(
#            first_name="john",
# 			last_name="owuor",
# 			regestration_number="6677",
# 			place_of_resident="Nairobi",
# 			phone_number="0788545456",
# 			email="chesangfelister@gmail.com",
# 			Id_number="98000",
# 			date_joined=datetime.date.today(),
# 			profession="mobile"
#            )
       
#         self.javascript = Course.objects.create(
#            name="javascript",
#             duration_in_months="4",
#             course_number="133334",
#             description="react applications",
#           )
#        	self.mobile = Course.objects.create(
#            name="mobile",
#             duration_in_months="3",
#             course_number="60862",
#             description="creating mobile apps",
#           )
#        	def test_teacher_can_have_many_courses(self):
#            self.assertEqual(self.teachers_a.courses.count(),0)
#            self.teachers_a.courses.add(self.javascript)
#            self.assertEqual(self.teachers_a.courses.count(),1)
#            self.teachers_a.courses.add(self.mobile)
#            self.assertEqual(self.teachers_a.courses.count(),2)