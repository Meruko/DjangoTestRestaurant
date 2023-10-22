# Generated by Django 4.2.6 on 2023-10-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dishes", "0004_alter_dish_ingridients"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="default_price",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="ingridient",
            name="price",
            field=models.FloatField(default=0.0),
        ),
    ]
