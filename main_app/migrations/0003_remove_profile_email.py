# Generated by Django 3.2.3 on 2021-05-18 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
