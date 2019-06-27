from onlineapp.models import *
from django import forms


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college']
        widgets = {
            'name': forms.TextInput(attrs={"class": "input", "placeholder": "Enter student name"}),
            'email': forms.TextInput(attrs={"class": "input", "placeholder": "Enter email ID"}),
            'db_folder': forms.TextInput(attrs={"class": "input", "placeholder": "Folder name"}),
            'dropped_out': forms.CheckboxInput(attrs={"class": "input"}),
        }
