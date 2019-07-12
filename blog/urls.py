from django.urls import path
from . import views

urlpatterns=[
    path('post_list', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/',views.post_detail, name='post_detail'),
    path('post_new', views.post_new, name='post_new'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('login', views.login, name='login'),

]