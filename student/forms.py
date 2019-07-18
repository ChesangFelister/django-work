from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your first_name'}),required=True,max_length=50)
	last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your last_name'}),required=True,max_length=50)
	date_of_birth=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your date_of_birth'}),required=True)
	regestration_number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your regestration_number'}),required=True,max_length=50) 
	place_of_resident=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your place_of_resident'}),required=True,max_length=50)
	phone_number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your phone_number'}),required=True,max_length=50)
	email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your email'}),required=True,max_length=50)
	guardian_phone_number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your phone_number'}),required=True,max_length=50)
	Id_number=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your Id_number'}),required=True)
	date_joined=forms.DateField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":'enter your date_joined'}),required=True)
		
		

	class Meta:
		model=Student
		fields="__all__"
		