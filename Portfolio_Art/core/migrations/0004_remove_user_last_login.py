# Generated by Django 5.0 on 2023-12-30 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
