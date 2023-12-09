from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from gestione_oggetti.models import Item

from .models import CustomUser as User

class Acquirenti:

    def __init__(self):
        self.nome_gruppo = "Acquirenti"
        self.group, self.created = Group.objects.get_or_create(name= self.nome_gruppo)
        self.group.save()
        self.crea_gruppo()
        self.__permessi__()

    def crea_gruppo(self):
        if self.created:
            print(f"Gruppo '{self.nome_gruppo}' creato con successo.")
        else:
            print(f"Il gruppo '{self.nome_gruppo}' esiste già.")

    def assegna_utente_al_gruppo(self, email_utente):
        try:
            # Ottenere l'utente
            utente = User.objects.get(email= email_utente)

            # Assegnare l'utente al gruppo
            self.group = Group.objects.get(name=self.nome_gruppo)
            self.group.user_set.add(utente)
            print(f"Utente '{utente.username}' assegnato al gruppo '{self.nome_gruppo}'.")
        except User.DoesNotExist:
            print(f"L'utente con la seguente email'{email_utente}' non esiste.")
        except Group.DoesNotExist:
            print(f"Il gruppo '{self.nome_gruppo}' non esiste.")

    def visualizza_gruppi_utente_e_permessi(self, email_utente):
        try:
            # Ottenere l'utente
            utente = User.objects.get(email= email_utente)

            # Visualizzare i gruppi dell'utente
            groups = utente.groups.all()
            print(f"Gruppi dell'utente '{utente.username}':")
            for group in groups:
                print(f"- {group.name}")

            # Visualizzare i permessi del gruppo
            try:
                group = Group.objects.get(name=self.nome_gruppo)
                permissions = group.permissions.all()
                print(f"\nPermessi del gruppo '{self.nome_gruppo}':")
                for permission in permissions:
                    print(f"- {permission}")
            except Group.DoesNotExist:
                print(f"Il gruppo '{self.nome_gruppo}' non esiste.")

        except User.DoesNotExist:
            print(f"L'utente con l'email '{email_utente}' non esiste.")

    def get_group_members(self):
        try:
            # Ottenere i membri del gruppo
            group = Group.objects.get(name=self.nome_gruppo)
            members = group.user_set.all()
            print(f"Membri del gruppo '{self.nome_gruppo}':")
            for member in members:
                print(f"- {member.username}")
        except Group.DoesNotExist:
            print(f"Il gruppo '{self.nome_gruppo}' non esiste.")

    def __permessi__(self):
        todoitem_content_type = ContentType.objects.get_for_model(Item)

        change_offer_permission = Permission.objects.get_or_create(
            codename='change_offer',
            content_type=todoitem_content_type,
            name="Può modificare il prezzo dell' offerta"
        )[0]

        self.group.permissions.add(change_offer_permission)