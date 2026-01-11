from django.urls import path
from .views import *

urlpatterns = [
    path('hello_world', hello_world, name='hello_world'),
    path('hello/<str:url_thing>', hello_thing, name='hello_thing')
]
