from django.urls import path
from . import views
from .views import LoginView, register_view, user_info_view, item_awarded

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('user_info/', user_info_view, name='profilo'),
    path('user_info_aste_aggiudicate/', item_awarded, name='oggetti_aggiudicati'),
]
