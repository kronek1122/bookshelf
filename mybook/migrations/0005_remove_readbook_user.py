# Generated by Django 4.2.7 on 2023-12-21 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybook', '0004_readbook_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readbook',
            name='user',
        ),
    ]
