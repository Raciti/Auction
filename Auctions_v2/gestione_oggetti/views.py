from django.views.generic import ListView
from .models import Item


class AllToDos(ListView):
    model = Item
    template_name = "tutte_aste.html"

    def get_queryset(self):
        return Item.objects.all().order_by('-timer')


class TodayToDos(ListView):
    model = Item
    template_name = "aste_giorno.html"

    def get_queryset(self):
        return Item.objects.all().order_by('-timer')


class ActiveToDos(ListView):
    model = Item
    template_name = "aste_attive.html"

    def get_queryset(self):
        return Item.objects.all().order_by('timer').order_by('-offer')

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from .middleware import GroupRequiredMixin


@method_decorator(GroupRequiredMixin('Acquirenti'), name='dispatch')
class ModificaOfferView(View):
    template_name = 'modifica_offer.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(Item, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})

    def post(self, request, todoitem_id):
        print(request)
        todoitem = get_object_or_404(Item, pk=todoitem_id)

        new_offer_value = request.POST.get('new_offer')

        if float(new_offer_value) < todoitem.min_sale:
            messages.error(request, "L'offerta deve essere maggiore del prezzo di partenza.")
            return render(request, self.template_name, {'todoitem': todoitem})

        if float(new_offer_value) <= todoitem.offer:
            messages.error(request, "L'offerta deve essere maggiore di quella attuale.")
            return render(request, self.template_name, {'todoitem': todoitem})

        if not todoitem.available():
            messages.error(request, "Il tempo per fare offerte è scaduto.")
            return render(request, self.template_name, {'todoitem': todoitem})

        current_user = request.user
        todoitem.offer = new_offer_value
        todoitem.user = current_user
        todoitem.save()

        return render(request, self.template_name, {'todoitem': todoitem})


from django.views import View


class DettaglioProdottoView(View):
    template_name = 'dettaglio_prodotto.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(Item, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})