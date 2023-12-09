from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.message_list, name='message_list'),
    path('send/', views.send_message, name='send_message'),
]
