from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.shortcuts import redirect
def add_student(request):
	# form=StudentForm()
	# return render(request,"add_student.html",{"form":form})

	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form=StudentForm()
	return render(request,"add_student.html",{"form":form})

def list_student(request):
	student=Student.objects.all()
	return render(request,"list_student.html",{"student":student})

def student_detail(request,pk):
	student=Student.objects.get(pk=pk)
	return render(request,"student_detail.html",{"student":student})

def edit_student(request,pk):
	student=Student.objects.get(pk=pk)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
			return redirect("add_student")
	else:
		form=StudentForm(instance=student)
		return render(request,"edit_student.html",{"form":form})

def edit_student(request,pk):
	student=Student.objects.get(pk=pk)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
			return redirect("list_student")
	else:
		form=StudentForm(instance=student)
		return render(request,"edit_student.html",{"form":form})


# Create your views here.
