from django.urls import path
from .views import add_course
from .views import list_course
from .views import course_detail
from .views import edit_course

urlpatterns=[
path("add/",add_course,name="add_course"),
path("list/",list_course,name="list_course"),
path("detail/<int:pk>/",course_detail,name="course_add"),
path("edit/<int:pk>/",edit_course,name="edit_course")
]