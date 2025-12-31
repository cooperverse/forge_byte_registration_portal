from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Register, AcademicQualification
class RegisterForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'email', 'roll', 'fathers_name', 'date_of_birth', 'phone', 'gender','department', 'course', 'student_photo', 'city', 'address']
        

AcademicFormSet = inlineformset_factory(
    Register, AcademicQualification,
    fields= ['exam_name', 'institute_name', 'group_subject', 'board_university', 'passing_year', 'gpa'],
    extra=4, can_delete=False
    )