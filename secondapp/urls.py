from django.urls import path
from . import views

urlpatterns=[
    path('address3', views.secondapp_practice, name='secondapp_1')
]