# Generated by Django 4.2.3 on 2023-07-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_delete_series"),
    ]

    operations = [
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1000)),
                ("plot", models.CharField(max_length=1000)),
                ("year", models.DateField()),
                ("seasons", models.CharField(max_length=1000)),
                ("genre", models.CharField(max_length=1000)),
                ("writer", models.CharField(max_length=1000)),
                ("rating", models.FloatField()),
                ("poster", models.CharField(max_length=1000)),
            ],
        ),
    ]