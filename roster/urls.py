from django.urls import path
from roster.views import (load_roster)

from . import views

app_name = 'roster'
urlpatterns = [
    path('', load_roster, name='load_roster'),
]