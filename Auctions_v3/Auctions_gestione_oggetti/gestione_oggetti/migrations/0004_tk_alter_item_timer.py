# Generated by Django 4.2.8 on 2023-12-15 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestione_oggetti', '0003_alter_item_timer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tk', models.CharField(max_length=100000)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='timer',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 11, 5, 9, 762540, tzinfo=datetime.timezone.utc)),
        ),
    ]
