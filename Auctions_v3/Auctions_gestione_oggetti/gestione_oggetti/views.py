from django.http import JsonResponse
from django.views.generic import ListView

from .models import Item


class AllToDos(ListView):
    model = Item
    template_name = "item/tutte_aste.html"


    def get_queryset(self):
        return Item.objects.all().order_by('-timer')



class TodayToDos(ListView):
    model = Item
    template_name = "item/aste_giorno.html"

    def get_queryset(self):
        return Item.objects.all().order_by('-timer')


class ActiveToDos(ListView):
    model = Item
    template_name = "item/aste_attive.html"

    def get_queryset(self):
        return Item.objects.all().order_by('timer').order_by('-offer')

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages


class ModificaOfferView(View):
    template_name = 'item/modifica_offer.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(Item, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})

    def post(self, request, todoitem_id):
        todoitem = get_object_or_404(Item, pk=todoitem_id)

        new_offer_value = request.POST.get('new_offer')

        if float(new_offer_value) < todoitem.min_sale:
            messages.error(request, "L'offerta deve essere maggiore del prezzo di partenza.")
            return render(request, self.template_name, {'todoitem': todoitem})

        if "." in str(new_offer_value) or "," in str(new_offer_value):
            messages.error(request, "L'offerta non può contenere centesimi.")
            return render(request, self.template_name, {'todoitem': todoitem})

        if float(new_offer_value) <= todoitem.offer:
            messages.error(request, "L'offerta deve essere maggiore di quella attuale.")
            return render(request, self.template_name, {'todoitem': todoitem})

        if not todoitem.available():
            messages.error(request, "Il tempo per fare offerte è scaduto.")
            return render(request, self.template_name, {'todoitem': todoitem})


        todoitem.offer = new_offer_value
        todoitem.user = Quest.objects.last().get_email()
        todoitem.save()

        return render(request, self.template_name, {'todoitem': todoitem})


from django.views import View


class DettaglioProdottoView(View):
    template_name = 'item/dettaglio_prodotto.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(Item, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})


from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings
from gestione_oggetti.models import Quest

@csrf_exempt
def tua_view(request):
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        _, token = auth_header.split(' ')

        try:

            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_email = decoded_token.get('user_email')
            username = decoded_token.get('user_username')
            name = decoded_token.get('user_name')

            quest = Quest()
            quest.set_tk(token)
            quest.save()

            message = f"Richiesta ricevuta con successo. Utente associato all'email: {user_email}, con username: {username}"
            return JsonResponse({"message": message})
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token scaduto"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token non valido"}, status=401)
    else:
        return JsonResponse({"error": "Token mancante nell'header Authorization"}, status=401)

@csrf_exempt
def view_oggetti(request):
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        _, token = auth_header.split(' ')

        try:

            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_email = decoded_token.get('user_email')
            username = decoded_token.get('user_username')
            name = decoded_token.get('user_name')

            quest = Quest()
            quest.set_tk(token)
            quest.save()

            object_list = Item.objects.all()
            oggetti_aggiudicati = [item for item in object_list if item.check_User(quest.get_email()) == True and item.available() == False]
            oggetti_aggiudicati = [{"text": item.text, "min_sale": item.min_sale, "offer": item.offer} for item in oggetti_aggiudicati]

            return JsonResponse({"oggetti_aggiudicati": str(oggetti_aggiudicati)})
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token scaduto"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token non valido"}, status=401)
    else:
        return JsonResponse({"error": "Token mancante nell'header Authorization"}, status=401)
