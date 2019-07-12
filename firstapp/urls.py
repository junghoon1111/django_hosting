from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('address', views.second, name='second_2'),
    path('address2', views.third, name='second_3'),

]

