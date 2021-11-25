from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('roster/', include('roster.urls')),
    path('admin/', admin.site.urls),
]