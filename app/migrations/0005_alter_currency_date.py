# Generated by Django 4.0 on 2022-07-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_order_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='date',
            field=models.DateField(max_length=64, null=True),
        ),
    ]
