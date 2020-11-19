from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', symmetrical=True,
                                     through='Friendship', through_fields=('sender', 'receiver',))

    def __str__(self):
        return self.name

class Friendship(models.Model):
    '''REQUESTED = 'REQUESTED'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'

    STATUS_CHOICES = (
        (REQUESTED, 'requested'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
    )

    status = models.TextField(choices=STATUS_CHOICES, default=REQUESTED)'''
    sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='friendship_sender')
    receiver = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='frinedship_receiver')

    def __str__ (self):
        return f"{self.sender} {self.receiver}"


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