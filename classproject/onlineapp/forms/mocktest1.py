from onlineapp.models import *
from django import forms


class AddMockTest1(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'student', 'total']
        widgets = {
            'problem1': forms.TextInput(attrs={"class": "input", "placeholder": "Score of problem1"}),
            'problem2': forms.TextInput(attrs={"class": "input", "placeholder": "Score of problem2"}),
            'problem3': forms.TextInput(attrs={"class": "input", "placeholder": "Score of problem3"}),
            'problem4': forms.TextInput(attrs={"class": "input", "placeholder": "Score of problem4"}),
        }
