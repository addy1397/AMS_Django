from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import PassengerLogin,BookTicket,EmployeeLogin
from .models import Passenger,Ticket,Employee,Flight
from random import randint

def index(request):
    form=PassengerLogin(request.POST)
    if form.is_valid() :
        cd=form.cleaned_data
        id=cd['id']
        name=cd['name']
        passenger = Passenger.objects.get(id=id)
        if passenger.firstName == name:
            return render(request, 'ticketing/detail.html', {'passenger':passenger})
        else:
            return render(request, 'ticketing/index.html', {'form':form})
    return render(request, 'ticketing/index.html', {'form':form})

def detail(request,id):
    return render(request, 'ticketing/detail.html', {'id':id})

def ticket(request, id):
    tickets=Ticket.objects.filter(passenger=Passenger.objects.get(id=id))
    return render(request, 'ticketing/ticket.html', {'ticket':tickets})

def cancel(request, id):
    tempTicket = Ticket.objects.filter(id=id)
    tempTicket.delete()
    return render(request, 'ticketing/cancel.html')

def book(request, id):
    form=BookTicket(request.POST)
    if form.is_valid() :
        cd=form.cleaned_data
        source=cd['source']
        destination=cd['destination']
        _class=cd['_class']
        iD=randint(100,100000)
        price=randint(4000,10000)
        passenger = Passenger.objects.get(id=id)
        ticket=Ticket(source=source,
            destination=destination,
            _class=_class,
            id=iD,
            price=price,
            passenger=passenger,
            )
        ticket.save()
        return render(request, 'ticketing/confirm.html', {'id':id})
    return render(request, 'ticketing/book.html', {'form':form})

def confirm(request, id):
    return render(request, 'ticketing/confirm.html', {'id':id})

def employee(request):
    form=EmployeeLogin(request.POST)
    if form.is_valid() :
        cd=form.cleaned_data
        name=cd['name']
        employee = Employee.objects.get(firstName=name)
        return render(request, 'ticketing/employeeDetail.html', {'employee':employee})
    return render(request, 'ticketing/employee.html', {'form':form})

def flight(request):
    temp=Flight.objects.all()
    return render(request, 'ticketing/flight.html',{'flight':temp})
