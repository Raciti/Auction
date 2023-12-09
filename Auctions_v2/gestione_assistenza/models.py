from django.db import models
from gestione_utenti.models import CustomUser as User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender:{self.sender} -> {self.content}"
