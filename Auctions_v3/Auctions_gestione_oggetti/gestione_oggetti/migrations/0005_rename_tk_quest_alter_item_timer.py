# Generated by Django 4.2.8 on 2023-12-15 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_oggetti', '0004_tk_alter_item_timer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tk',
            new_name='Quest',
        ),
        migrations.AlterField(
            model_name='item',
            name='timer',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 11, 9, 47, 110147, tzinfo=datetime.timezone.utc)),
        ),
    ]
