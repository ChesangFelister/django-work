# from course.models import Course
# from teacher.models import Teacher
# from django.test import TestCase
# import datetime
# class CourseTeacherTestCase(TestCase):
#    def setUp(self):
#        self.teacher_a = Teacher.objects.create(
#         first_name="lucy",
#         last_name="Njeri",
#         regestration_number="6677865",
#         place_of_resident="Nairobi",
#         phone_number="076533323",
#         email="chesangfelister@gmail.com",
#         Id_number="987768787",
#         date_joined=datetime.date.today(),
#         profession="Developer"
#        )
#        self.teacher_b = Teacher.objects.create(

#         first_name="john",
#         last_name="owuor",
#         regestration_number="6677",
#         place_of_resident="Nairobi",
#         phone_number="0788545456",
#         email="chesangfelister@gmail.com",
#         Id_number="98000",
#         date_joined=datetime.date.today(),
#         profession="mobile")

#        self.python = Course.objects.create(
#           name="python",
#           duration_in_months="4",
#           course_number="667000",
#           description="data",
#        )

#    def test_course_cannot_have_many_teachers(self):
#     self.python.teacher = self.teacher_a
#     self.python.teacher = self.teacher_b
#     self.assertTrue(self.python.teacher==self.teacher_a)
 











































#    # def test_many_courses_can_have_one_trainer(self):
#    #     self.electronics.teacher = self.teacher_b
#    #     self.hardware_design.teacher = self.teacher_b
#    #     self.assertEqual(self.electronics.teacher, self.hardware_design.teacher)

 
#          # self.hardware_design = Course.objects.create(
#        #     name="hardware design",
#        #      duration_in_months="9",
#        #      course_number="66007",
#        #      description="design",

#        # )
#   # self.electronics = Course.objects.create(
#   #         name="Electronics",
#   #         duration_in_months="7",
#   #         course_number="667765",
#   #         description="electronics",

#   #      )