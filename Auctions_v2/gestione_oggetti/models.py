from datetime import timedelta
from gestione_utenti.models import CustomUser as User
from django.utils import timezone
from django.db import models

class Item(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)
    min_sale = models.IntegerField(default=1)
    timer = models.DateTimeField(default=timezone.now() + timedelta(hours=1))
    offer = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def tempo_rimanente(self):
        now = timezone.now()
        time_difference = self.timer - now
        if now > self.timer:
            return "Scaduto"
        else:
            return time_difference

    def available(self):
        now = timezone.now()
        if now > self.timer:
            return False
        else:
            return True

    def venduto(self):
        if self.min_sale != self.offer and self.available() == False:
            return True
        else:
            return False

    def check_User(self, u):
        return str(self.user) == str(u)

    def getCaricamento(self):
        return self.due_date == timezone.now().date()

    def __str__(self):
        return f"{self.text}: Prezzo partenza {self.min_sale}, Tempo rimanente: {self.timer}, Data aggiunta: {self.due_date}. "
