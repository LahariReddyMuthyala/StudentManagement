from django.views import View
from onlineapp.models import *
from onlineapp.forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class AddStudentView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form1 = AddStudent()
        form2 = AddMockTest1()
        if kwargs.get('student_id'):
            student = Student.objects.get(id=kwargs.get('student_id'))
            mocktest1 = MockTest1.objects.get(student_id=kwargs.get('student_id'))
            form1 = AddStudent(instance=student)
            form2 = AddMockTest1(instance=mocktest1)
        return render(
            request,
            'add_student.html',
            {'form1': form1, 'form2': form2, 'title': "Add student", 'logged_in': request.user.is_authenticated})

    def post(self, request, *args, **kwargs):
        form1 = AddStudent(request.POST)
        form2 = AddMockTest1(request.POST)
        if kwargs.get('student_id'):
            student = Student.objects.get(id=kwargs.get('student_id'))
            mocktest1 = MockTest1.objects.get(student_id=kwargs.get('student_id'))
            form1 = AddStudent(request.POST, instance=student)
            form2 = AddMockTest1(request.POST, instance=mocktest1)
            college = get_object_or_404(College, id=kwargs.get('college_id'))
        else:
            form1 = AddStudent(request.POST)
            form2 = AddMockTest1(request.POST)
            college = get_object_or_404(College, id=kwargs.get('college_id'))
        if form1.is_valid() and form2.is_valid():
            student = form1.save(commit=False)
            student.college = college
            student.save()
            mocktest1 = form2.save(commit=False)
            mocktest1.student = student
            mocktest1.total = str(mocktest1.problem1+mocktest1.problem2+mocktest1.problem3+mocktest1.problem4)
            mocktest1.save()
            return redirect('colleges_html')


class DeleteStudentView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        if kwargs.get('student_id'):
            mocktest1 = get_object_or_404(MockTest1, student_id=kwargs.get('student_id'))
            mocktest1.delete()
            student = get_object_or_404(Student, id=kwargs.get('student_id'))
            student.delete()
        return redirect('colleges_html')