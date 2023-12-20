from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from Auctions_gestione_utenti.settings import SECRET_KEY
from .forms import LoginForm
from django.http import JsonResponse


def generate_jwt_token(user):
    return jwt.encode({'user_email': user.email, 'user_username': user.username}, SECRET_KEY,
                      algorithm='HS256')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Profilo/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        token = generate_jwt_token(user)
        user.set_tk(token)
        response = super().form_valid(form)
        response.data = {'token': token}
        user.save()

        return redirect('home')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.data = {'error': 'Credenziali non valide'}
        return response


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            token = generate_jwt_token(user)
            user.set_tk(token)
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'Profilo/register.html', {'form': form})



from .models import CustomUser as User
def user_info_view(request):
    if not request.user.is_authenticated:
        user = User.objects.filter(last_login__isnull=False).order_by('-last_login').first()
        login(request, user)
    return render(request, 'Profilo/profilo.html')

def item_awarded(request):
    return render(request, 'Profilo/aste_vinte.html')

import jwt
from django.conf import settings

@csrf_exempt
def view(request):
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        _, token = auth_header.split(' ')

        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            user_email = decoded_token.get('user_email')
            username = decoded_token.get('user_username')

            message = f"Richiesta ricevuta con successo. Utente associato all'email: {user_email}, con username: {username}"

            user = User.objects.get(email=user_email)
            login(request, user)

            return JsonResponse({"message": message})
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token scaduto"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token non valido"}, status=401)
    else:
        return JsonResponse({"error": "Token mancante nell'header Authorization"}, status=401)


def home_view(request):
    user = User.objects.filter(last_login__isnull=False).order_by('-last_login').first()
    login(request, user)
    return render(request, 'home.html')