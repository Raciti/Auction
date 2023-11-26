from django.urls import path
from . import views
from .views import SignUpView, CustomPasswordResetView, user_info_view, ModificaOfferView, DettaglioProdottoView, \
    LoginView

urlpatterns = [
    path("today/", views.TodayToDos.as_view(), name="today"),
    path("all/", views.AllToDos.as_view(), name="all"),
    path("active/", views.ActiveToDos.as_view(), name="active"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name='login'),
    path("", views.AllToDos.as_view(), name="home"),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', CustomPasswordResetView.as_view(), name='password_reset_done'),
    path('user-info/', user_info_view, name='profilo'),
    path("item/<int:todoitem_id>/", DettaglioProdottoView.as_view(), name="dettaglio_prodotto"),
    path("item/<int:todoitem_id>/modifica-offerta/", ModificaOfferView.as_view(), name="modifica_offerta"),
]
