# Generated by Django 2.2.1 on 2019-05-27 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20190527_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='api_key',
            new_name='uuid',
        ),
    ]
