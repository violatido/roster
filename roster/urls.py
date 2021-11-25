from django.urls import path
from roster.views import (load_roster, update_vote_count)

from . import views

app_name = 'roster'
urlpatterns = [
    path('', load_roster, name='load_roster'),
    path('update-vote-count', update_vote_count, name='update_vote_count'),
]