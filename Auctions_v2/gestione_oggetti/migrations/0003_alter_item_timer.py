# Generated by Django 4.2.7 on 2023-12-04 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_oggetti', '0002_item_delete_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='timer',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 10, 38, 47, 284106, tzinfo=datetime.timezone.utc)),
        ),
    ]
