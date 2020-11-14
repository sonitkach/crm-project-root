from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        add = self.name or '[no name]'
        return f'<Company "{add}">'


class Speciality(models.Model):
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.speciality


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)

    def full_name(self):
        return f"{self.name} {self.surname}"