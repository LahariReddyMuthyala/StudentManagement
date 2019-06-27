from django.views import View
from onlineapp.models import *
from onlineapp.forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import logging

class CollegeView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        if kwargs:
            college = get_object_or_404(College, id=kwargs.get('college_id'))
            studentDetails = Student.objects.values('id', 'name', 'email', 'mocktest1__total').filter(college__id=kwargs.get('college_id')).order_by("-mocktest1__total")
            user_permissions = request.user.get_all_permissions()
            return render(
                request,
                template_name='college_details.html',
                context={
                    'college': college,
                    'studentDetails': studentDetails,
                    'title': 'Students of {} | class project'.format(college.name),
                    'user_permissions': user_permissions,
                    'logged_in': request.user.is_authenticated
                }
            )

        colleges=College.objects.all()
        user_permissions = request.user.get_all_permissions()
        logging.error('Error')
        return render(
            request,
            template_name="colleges.html",
            context={
                'colleges': colleges,
                'title': 'All colleges | Class Project',
                'user_permissions': user_permissions,
                'logged_in': request.user.is_authenticated
            }
        )


class AddCollegeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = AddCollege()
        if kwargs:
            college = College.objects.get(id=kwargs.get('id'))
            form = AddCollege(instance=college)

        return render(request, 'add_college.html', {'form': form, 'title': 'Add college', 'logged_in': request.user.is_authenticated})

    def post(self, request, *args, **kwargs):
        form = AddCollege(request.POST)
        if kwargs:
            college = College.objects.get(id=kwargs.get('id'))
            form = AddCollege(request.POST, instance=college)
            if form.is_valid():
                form.save()
            return redirect('colleges_html')
        form = AddCollege(request.POST)
        if form.is_valid():
            form.save()
        return redirect('colleges_html')


class DeleteCollegeView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        if kwargs:
            college = get_object_or_404(College, id=kwargs.get('college_id'))
            college.delete()
        return redirect('colleges_html')



