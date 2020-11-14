from rest_framework import serializers

from .models import Company, Speciality, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('speciality',)


class EmployeeSerializer(serializers.ModelSerializer):

    company = CompanySerializer()
    speciality = SpecialitySerializer()

    class Meta:
        model = Employee
        fields = ('name', 'surname', 'company', 'speciality',)