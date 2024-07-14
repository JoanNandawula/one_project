# Generated by Django 5.0.3 on 2024-07-14 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_shopform_total_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shopform",
            name="total_amount",
        ),
        migrations.AlterField(
            model_name="shopform",
            name="Date_of_purchase",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 14, 17, 13, 52, 336770, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
