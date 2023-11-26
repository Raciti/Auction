from datetime import date

from django.views.generic import ListView
from .models import ToDoItem

class AllToDos(ListView):
    model = ToDoItem
    template_name = "Auctions/index.html"

    def get_queryset(self):
        return ToDoItem.objects.all().order_by('-timer')
class TodayToDos(ListView):
    model = ToDoItem
    template_name = "Auctions/today.html"

    def get_queryset(self):
        return ToDoItem.objects.all().order_by('-timer')

class ActiveToDos(ListView):
    model = ToDoItem
    template_name = "Auctions/attive.html"

    def get_queryset(self):
        return ToDoItem.objects.all().order_by('timer').order_by('-offer')



from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .form import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Registration/login.html'

from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .form import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "Registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)

            # Aggiungi l'utente al gruppo "Acquirenti"
            acquirenti_group = Group.objects.get(name='Acquirenti')
            user.groups.add(acquirenti_group)

            # Reindirizza alla vista principale
            return redirect('all')

        return super().form_invalid(form)


# views.py
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django import forms

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'Registration/password_reset_form.html'


# views.py
from django.shortcuts import render
from django.contrib.auth.models import User  # Supponiamo che tu stia utilizzando il modello User di Django

def user_info_view(request):
    user = User.objects.get(username=request.user.username)
    print("CIAO")
    object_list = ToDoItem.objects.all()

    # Eseguire la logica della tua funzione Check_User e ottenere la lista filtrata
    user_name = user.username  # Verifica se il campo corretto è 'name'
    oggetti_aggiudicati = [item for item in object_list if item.check_User(user_name) == True]
    print(oggetti_aggiudicati)

    return render(request, 'User/profilo.html', {'user': user, 'oggetti_aggiudicati': oggetti_aggiudicati})


#Modifica offer
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import ToDoItem
from django.http import HttpResponseBadRequest
from django.contrib import messages
from .middleware import GroupRequiredMixin

@method_decorator(GroupRequiredMixin('Acquirenti'), name='dispatch')
class ModificaOfferView(View):
    template_name = 'Auctions/modifica_offer.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(ToDoItem, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})

    def post(self, request, todoitem_id):
        print(request)
        todoitem = get_object_or_404(ToDoItem, pk=todoitem_id)

        # Processa la richiesta POST per modificare il campo offer
        new_offer_value = request.POST.get('new_offer')

        # Controlla se l'offerta è maggiore del prezzo di partenza
        if float(new_offer_value) < todoitem.min_sale:
            messages.error(request, "L'offerta deve essere maggiore del prezzo di partenza.")
            return render(request, self.template_name, {'todoitem': todoitem})

        # Controlla se l'offerta è maggiore di quella attuale
        if float(new_offer_value) <= todoitem.offer:
            messages.error(request, "L'offerta deve essere maggiore di quella attuale.")
            return render(request, self.template_name, {'todoitem': todoitem})

        # Controlla se l'offerta è ammissibile in base al tempo rimanente
        if not todoitem.available():
            messages.error(request, "Il tempo per fare offerte è scaduto.")
            return render(request, self.template_name, {'todoitem': todoitem})

        current_user = request.user
        todoitem.offer = new_offer_value
        todoitem.user = current_user
        todoitem.save()

        return render(request, self.template_name, {'todoitem': todoitem})



from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ToDoItem

class DettaglioProdottoView(View):
    template_name = 'Auctions/dettaglio_prodotto.html'

    def get(self, request, todoitem_id):
        todoitem = get_object_or_404(ToDoItem, pk=todoitem_id)
        return render(request, self.template_name, {'todoitem': todoitem})
