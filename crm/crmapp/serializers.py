from rest_framework import serializers

from .models import Company, Speciality, Employee, Friendship


class CompanySerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ('name', 'friends',)


class FriendshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friendship
        fields = ('sender', 'receiver',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sender'] = CompanySerializer(instance.sender).data
        response['receiver'] = CompanySerializer(instance.receiver).data
        return response


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('speciality',)


class EmployeeSerializer(serializers.ModelSerializer):

    #company = CompanySerializer()
    #speciality = SpecialitySerializer()

    class Meta:
        model = Employee
        fields = ('name', 'surname', 'company', 'speciality',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        response['speciality'] = SpecialitySerializer(instance.speciality).data
        return response

    '''
    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company_model = Company.objects.create(**company_data)

        speciality_data = validated_data.pop('speciality')
        speciality_model = Speciality.objects.create(**speciality_data)

        employee = Employee.objects.create(company=company_model, speciality = speciality_model, **validated_data)
        return employee
    '''