"backoffice URL Configuration"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="mus_index" )
    
]
