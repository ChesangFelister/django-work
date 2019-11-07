from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher
from django.http import HttpResponseBadRequest

def add_teacher(request):
	# form=TeacherForm()
	# return render(request,"add_teacher.html",{"form":form})

	if request.method=="POST":
		form=TeacherForm(request.POST)

		if form.is_valid():
			form.save()
		

		else:
			return HttpResponseBadRequest()	
	else:
		form=TeacherForm()
	return render(request,"add_teacher.html",{"form":form})
def list_teachers(request):
	teachers=Teacher.objects.all()
	return render(request,"list_teachers.html",{"teachers":teachers})




def teacher_detail(request,pk):
	teachers=Teacher.objects.get(pk=pk)
	return render(request,"teacher_detail.html",{"teachers":teachers})

def edit_teacher(request,pk):
	teachers=Teacher.objects.get(pk=pk)
	if request.method=="POST":
		form=TeacherForm(request.POST,instance=teachers)
		if form.is_valid():
			form.save()
			return redirect("add_teacher")
	else:
		form=TeacherForm(instance=teachers)
		return render(request,"edit_teacher.html",{"form":form})


def edit_teacher(request,pk):
	teachers=Teacher.objects.get(pk=pk)
	if request.method=="POST":
		form=TeacherForm(request.POST,instance=teachers)
		if form.is_valid():
			form.save()
			return redirect("list_teachers")
	else:
		form=TeacherForm(instance=teachers)
		return render(request,"edit_teacher.html",{"form":form})


# Create your views here.
