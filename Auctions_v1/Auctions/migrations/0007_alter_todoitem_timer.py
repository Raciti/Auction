# Generated by Django 4.2.7 on 2023-11-25 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auctions', '0006_alter_todoitem_timer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='timer',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 18, 58, 3, 187532, tzinfo=datetime.timezone.utc)),
        ),
    ]
