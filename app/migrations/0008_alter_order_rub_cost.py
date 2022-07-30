# Generated by Django 4.0 on 2022-07-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_currency_usd_rub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rub_cost',
            field=models.DecimalField(decimal_places=4, max_digits=7, null=True),
        ),
    ]