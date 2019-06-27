from django.views import View
from onlineapp.models import *
from onlineapp.forms import *
from onlineapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from django.shortcuts import  get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class student_details(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        if kwargs.get('spk'):
            college = get_object_or_404(College,pk=kwargs.get('cpk'))
            student = get_object_or_404(Student, pk=kwargs.get('spk'), college_id=college)
            serializer = StudentDetailsSerializer(student, many=False)
            return Response(serializer.data)
        college = get_object_or_404(College,pk=kwargs.get('cpk'))
        student = Student.objects.filter(college_id=college)
        serializer = StudentDetailsSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentDetailsSerializer(data=request.data, context={'cpk': kwargs['cpk']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('spk'):
            college = get_object_or_404(College,pk=kwargs.get('cpk'))
            student = get_object_or_404(Student, pk=kwargs.get('spk'), college_id=college)
            serializer = StudentDetailsSerializer(student, data=request.data, many=False, context={'cpk': kwargs['cpk'], 'spk': kwargs['spk']})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('spk'):
            college = get_object_or_404(College, pk=kwargs.get('cpk'))
            student = get_object_or_404(Student, pk=kwargs.get('spk'), college_id=college)
            serializer = StudentDetailsSerializer(student, many=False)
            student.delete()
            return Response(serializer.data)


