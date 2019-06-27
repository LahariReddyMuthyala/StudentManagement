from onlineapp.models import *
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'location', 'acronym', 'contact')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'dob', 'email', 'db_folder', 'dropped_out', 'college')
    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        student.save()
        return student
    def update(self,instance, validated_data):
        self.instance.name = validated_data.get('name', self.instance.name)
        self.instance.email = validated_data.get('email', self.instance.email)
        self.instance.db_folder = validated_data.get('db_folder', self.instance.db_folder)
        self.instance.dropped_out = validated_data.get('dropped_out', self.instance.dropped_out)
        self.instance.save()
        return self.instance


class MockTest1Serializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('problem1', 'problem2', 'problem3', 'problem4', 'total')

    def create(self, validated_data):
        mocktest1 = MockTest1.objects.create(**validated_data)
        mocktest1.total = sum(validated_data.values())
        mocktest1.save()
        return mocktest1

    def update(self,instance, validated_data):
        instance.problem1 = validated_data.get('problem1', instance.problem1)
        instance.problem2 = validated_data.get('problem2', instance.problem2)
        instance.problem3 = validated_data.get('problem3', instance.problem3)
        instance.problem4 = validated_data.get('problem4', instance.problem4)
        validated_data.pop('total')
        instance.total = validated_data.get('total', sum(validated_data.values()))
        instance.save()
        return instance


class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest1 = MockTest1Serializer(many=False, read_only=False)
    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'db_folder', 'dropped_out', "mocktest1")
    def create(self, validated_data):
        mock = validated_data.pop('mocktest1')
        validated_data['college'] = College.objects.get(id=self.context['cpk'])
        student = Student.objects.create(**validated_data)
        MockTest1.objects.create(student=student, **mock)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
        instance.db_folder = validated_data.get('db_folder', instance.db_folder)
        mocktest1 = MockTest1Serializer(instance.mocktest1, data=dict(
            self._validated_data.get('mocktest1')
        ))
        if mocktest1.is_valid():
            mocktest1.save()
            instance.save()
        return instance












