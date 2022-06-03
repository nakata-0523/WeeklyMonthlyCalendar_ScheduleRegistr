from django.contrib import admin
from django.urls import path, include
from .views import MyCalendar

app_name = 'WeekMonthCalendarApp'

urlpatterns = [
    path('mycalendar/', MyCalendar.as_view(), name='mycalendar'),
    path('mycalendar/<int:year>/<int:month>/<int:day>/', MyCalendar.as_view(), name='mycalendar'),
]