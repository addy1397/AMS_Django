# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Passenger,Ticket,Flight,Airline,Airport,Employee

admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Employee)
