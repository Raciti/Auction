from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from gestione_assistenza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('messages/', views.message_list, name='message_list'),
    path('send/', views.send_message, name='send_message'),

    path('tua-view/', views.tua_view, name='tua_view'),

]
