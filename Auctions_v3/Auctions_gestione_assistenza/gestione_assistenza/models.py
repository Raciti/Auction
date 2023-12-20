from django.utils import timezone
import jwt
from django.db import models

from Auctions_gestione_assistenza import settings

class Message(models.Model):
    sender = models.CharField(max_length=1000000, default="")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sender:{self.sender} -> {self.content}"
class Quest(models.Model):
    tk = models.CharField(max_length=100000)
    due_date = models.DateTimeField(default=timezone.now)
    def set_tk(self, new_tk):
        self.tk = new_tk

    def get_tk(self):
        return  self.tk

    def get_username(self):
        decoded_token = jwt.decode(self.tk, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token.get('user_username')

    def get_email(self):
        decoded_token = jwt.decode(self.tk, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token.get('user_email')

    def get_name(self):
        decoded_token = jwt.decode(self.tk, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token.get('user_name')