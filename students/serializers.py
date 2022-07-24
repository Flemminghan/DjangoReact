from rest_framework import serializers
from .models import Student, Classroom

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student 
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom 
        fields = ('pk', 'name', 'location', 'registrationDate')