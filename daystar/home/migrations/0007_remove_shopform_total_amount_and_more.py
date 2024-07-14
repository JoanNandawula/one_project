# Generated by Django 5.0.3 on 2024-07-14 17:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_shopform_date_of_purchase"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shopform",
            name="Total_amount",
        ),
        migrations.AlterField(
            model_name="shopform",
            name="Date_of_purchase",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
