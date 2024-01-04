# Generated by Django 4.2.7 on 2023-12-21 19:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mybook', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserReview',
            new_name='UserOpinion',
        ),
        migrations.AddField(
            model_name='book',
            name='opinions',
            field=models.ManyToManyField(related_name='book_opinion', to='mybook.useropinion'),
        ),
    ]