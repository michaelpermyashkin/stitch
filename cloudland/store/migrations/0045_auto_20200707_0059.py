# Generated by Django 3.0.6 on 2020-07-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_auto_20200705_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_purchases',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=models.TextField(default='', help_text='Limit 100 characters: Brief discription of the item shown on the items detail view page', max_length=100),
        ),
    ]
