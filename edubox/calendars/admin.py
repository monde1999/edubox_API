from django.contrib import admin
from .models import Calendar, Event, Account, Membership

admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Account)
admin.site.register(Membership)