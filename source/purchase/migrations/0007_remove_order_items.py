# Generated by Django 4.2.11 on 2024-03-24 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
    ]
