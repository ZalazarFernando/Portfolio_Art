# Generated by Django 5.0 on 2024-01-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='post_id',
            new_name='post',
        ),
    ]
