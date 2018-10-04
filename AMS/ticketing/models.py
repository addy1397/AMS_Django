from __future__ import unicode_literals
from django.db import models

from datetime import datetime

class Passenger(models.Model):
    id=models.IntegerField(primary_key=True)
    age=models.IntegerField()
    sex=models.CharField(max_length=1)
    firstName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.firstName + " " + self.lastName + " (" + str(self.id) + ")"

class Ticket(models.Model):
    id=models.IntegerField(primary_key=True)
    price=models.IntegerField()
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    time=models.DateTimeField(default=datetime.now)
    _class=models.CharField(max_length=20)
    passenger=models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.source + " " + self.destination + " (" + str(self.id) + ")"

class Book(models.Model):
    dateOfBooking=models.DateTimeField('date booked')
    GSTNumber=models.IntegerField(default=0)
    passenger=models.ForeignKey(Passenger, on_delete=models.CASCADE)
    def __str__(self):
        return passenger.firstName + " with id " + str(passenger.id) + " booked the ticket"

class Cancel(models.Model):
    GSTNumber=models.IntegerField(default=0)
    cancellor=models.ForeignKey(Passenger, on_delete=models.CASCADE)
    date=models.DateTimeField('date cancelled')

    def __str__(self):
        return cancellor.firstName + " with id " + str(cancellor.id) + " cancelled the ticket"


class Flight(models.Model):
    type=models.CharField(max_length=20)
    flightCode=models.CharField(primary_key=True, max_length=3)
    arr=models.CharField(max_length=10)
    dep=models.CharField(max_length=30)
    soruce=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)

    def __str__(self):
        return self.source + " to " + self.destination + " with code " + self.flightCode


class Airline(models.Model):
    airlineId=models.IntegerField(primary_key=True)
    airlineName=models.CharField(max_length=30)
    code=models.CharField(max_length=10)

    def __str__(self):
        return self.airlineName + " (" + str(self.airlineId) + ")"



class Airport(models.Model):
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    tier=models.IntegerField()
    id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

class Employee(models.Model):
    SSN=models.IntegerField(primary_key=True)
    sex=models.CharField(max_length=1)
    age=models.IntegerField()
    firstName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    salary=models.IntegerField()
    phone=models.IntegerField()
    jobType=models.CharField(max_length=10)

    def __str__(self):
        return self.firstName + " " + self.lastName + " (" + str(self.SSN) + ")"
