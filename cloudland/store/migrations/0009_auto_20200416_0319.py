# Generated by Django 3.0.5 on 2020-04-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200416_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
