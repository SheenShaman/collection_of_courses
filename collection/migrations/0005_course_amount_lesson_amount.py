# Generated by Django 4.2.6 on 2023-11-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Сумма оплаты'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Сумма оплаты'),
        ),
    ]