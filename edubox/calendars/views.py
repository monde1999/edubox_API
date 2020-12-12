from rest_framework import viewsets
from django.views import View

from .serializers import CalendarSerializer, EventSerializer, AccountSerializer, AccountPrivateSerializer, MembershipSerializer
from .models import Calendar, Event, Account, Membership

class CalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all().filter(isDeleted=False).order_by('name')

    def get_queryset(self):
        queryset = Calendar.objects.all().filter(isDeleted=False).order_by('name')
        accountId = self.request.query_params.get('user', None)
        if accountId is not None:
            user_calendars = Membership.objects.all().filter(account=accountId, isDeleted=False)
            list_of_ids = []
            for cal in user_calendars:
                list_of_ids.append(cal.calendar.pk)
            queryset = queryset.filter(pk__in=list_of_ids)
        return queryset

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().filter(isDeleted=False).order_by('date', 'time')

    def get_queryset(self):
        queryset = Event.objects.all().filter(isDeleted=False).order_by('date', 'time')
        calendarId = self.request.query_params.get('calendar', None)
        if calendarId is not None:
            queryset = queryset.filter(calendar__id=calendarId)
        return queryset

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('username')
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.all().order_by('username')
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        if username is not None and password is not None:
            queryset = queryset.filter(username=username, password=password)
            self.serializer_class = AccountPrivateSerializer
        return queryset

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.filter(isDeleted=False)
    serializer_class = MembershipSerializer

    def get_queryset(self):
        queryset = Membership.objects.all().filter(isDeleted=False)
        calendarId = self.request.query_params.get('calendar', None)
        accountId = self.request.query_params.get('account', None)
        if calendarId is not None:
            if accountId is not None:
                queryset = queryset.filter(calendar__pk=calendarId, account__pk=accountId)
            else:
                queryset = queryset.filter(calendar__pk=calendarId)
                list_ids = []
                for id in queryset:
                    list_ids.append(id.account.id)
                print(list_ids)
                self.serializer_class = AccountSerializer
                queryset = Account.objects.filter(id__in=list_ids)
        return queryset