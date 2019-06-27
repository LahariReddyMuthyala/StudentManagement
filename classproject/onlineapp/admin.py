from django.contrib import admin

# Register your models here.

from .models import College, Student
admin.site.register(College)
admin.site.register(Student)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)