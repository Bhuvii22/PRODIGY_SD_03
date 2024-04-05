# Generated by Django 5.0.3 on 2024-03-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("cid", models.CharField(max_length=20)),
                ("cname", models.CharField(max_length=100)),
                ("cemail", models.EmailField(max_length=254)),
                ("ccontact", models.IntegerField(max_length=15)),
            ],
            options={
                "db_table": "customer",
            },
        ),
    ]