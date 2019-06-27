from django.views import View
from onlineapp.models import *
from onlineapp.forms import *
from onlineapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import  get_object_or_404

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def college_list(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs:
            college = get_object_or_404(College, pk = kwargs.get('cpk'))
            serializer = CollegeSerializer(college)
            return Response(serializer.data)
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        college = get_object_or_404(College, pk=kwargs.get('cpk'))
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        college = get_object_or_404(College, pk=kwargs.get('cpk'))
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



