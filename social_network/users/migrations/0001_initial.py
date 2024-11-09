# Generated by Django 5.1.3 on 2024-11-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=40)),
                ("e_mail", models.CharField(blank=True, max_length=20)),
                ("wallet_address", models.CharField(blank=True)),
            ],
        ),
    ]
