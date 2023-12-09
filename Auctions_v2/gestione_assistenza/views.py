from django.shortcuts import render
from .models import Message

def message_list(request):
    if request.user.is_staff:
        messages = Message.objects.all()
        return render(request, 'message_list.html', {'messages': messages})
    else:
        return render(request, 'home.html')

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Il messaggio è stato inviato con successo! Ti risponderemo al più presto controlla l'email utilizzata nella fase di registrazione.")
            return redirect('send_message')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
