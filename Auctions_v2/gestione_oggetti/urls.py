from django.urls import path
from . import views


urlpatterns = [
    path("tutte_aste/", views.AllToDos.as_view(), name="tutte_aste"),
    path("aste_giorno/", views.TodayToDos.as_view(), name="aste_giorno"),
    path("aste_attive/", views.ActiveToDos.as_view(), name="aste_attive"),
    path("item/<int:todoitem_id>/", views.DettaglioProdottoView.as_view(), name="dettaglio_prodotto"),
    path("item/<int:todoitem_id>/modifica-offerta/", views.ModificaOfferView.as_view(), name="modifica_offerta"),
]