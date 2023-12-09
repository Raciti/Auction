from django.contrib.auth import views as auth_views
from .forms import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .manage import Acquirenti
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            acquirenti_manager = Acquirenti()
            acquirenti_manager.assegna_utente_al_gruppo(user.email)


            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



from .models import CustomUser as User
from gestione_oggetti.models import Item
def user_info_view(request):
    return render(request, 'profilo.html')

def item_awarded(request):
    user = User.objects.get(username=request.user.username)
    object_list = Item.objects.all()

    user_name = user.email
    oggetti_aggiudicati = [item for item in object_list if item.check_User(user_name) == True]

    return render(request, 'aste_vinte.html', {'user': user, 'oggetti_aggiudicati': oggetti_aggiudicati})

