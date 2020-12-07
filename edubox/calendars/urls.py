from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'calendars', views.CalendarViewSet, )
router.register(r'events', views.EventViewSet, )
router.register(r'account', views.AccountViewSet)
router.register(r'membership', views.MembershipViewSet, )

app_name = 'calendar'

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]