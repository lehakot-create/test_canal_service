# Generated by Django 4.0 on 2022-07-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_order_rub_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
