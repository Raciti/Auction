from django.shortcuts import render
from .models import Message, Quest


def message_list(request):
    messages = Message.objects.all().order_by("-timestamp")
    return render(request, 'Assistenza/message_list.html', {'messages': messages})


from django.contrib import messages
from django.shortcuts import redirect
from .forms import MessageForm

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = Quest.objects.last().get_email()
            message.save()
            messages.success(request, "Il messaggio è stato inviato con successo! Ti risponderemo al più presto controlla l'email utilizzata nella fase di registrazione.")
            return redirect("send_message")
    else:
        form = MessageForm()
    return render(request, 'Assistenza/send_message.html', {'form': form})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings

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

            message = f"Richiesta ricevuta con successo. Utente associato all'email: {user_email}"
            return JsonResponse({"message": message})
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token scaduto"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token non valido"}, status=401)
    else:
        return JsonResponse({"error": "Token mancante nell'header Authorization"}, status=401)