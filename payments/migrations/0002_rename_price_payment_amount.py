# Generated by Django 4.2.6 on 2023-10-26 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='price',
            new_name='amount',
        ),
    ]
