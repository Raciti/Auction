# Generated by Django 4.2.7 on 2023-12-05 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_assistenza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
    ]