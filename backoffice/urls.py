"backoffice URL Configuration"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="bo_index" ),
    path('topic', views.topic, name="bo_topic" ),
    path('list_topics', views.list_topics, name="list_topic" ),
    path('sign', views.sign, name="sign" )

]
