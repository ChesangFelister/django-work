from django.urls import path
from .views import add_student
from .views import list_student
from .views import student_detail
from .views import edit_student

urlpatterns=[
path("add/",add_student,name="add_student"),
path("list/",list_student,name="list_student"),
path("detail/<int:pk>/",student_detail,name="student_add"),
path("edit/<int:pk>/",edit_student,name="edit_student")
]