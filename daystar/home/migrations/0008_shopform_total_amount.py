# Generated by Django 5.0.3 on 2024-07-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_remove_shopform_total_amount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopform",
            name="total_amount",
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
