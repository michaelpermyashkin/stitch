# Generated by Django 3.0.6 on 2020-06-25 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200603_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='phone_number',
        ),
    ]
