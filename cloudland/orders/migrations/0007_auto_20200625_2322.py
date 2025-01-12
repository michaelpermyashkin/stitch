# Generated by Django 3.0.6 on 2020-06-26 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_useraddress_phone_number'),
        ('orders', '0006_order_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='accounts.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='accounts.UserAddress'),
        ),
    ]
