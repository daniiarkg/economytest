# Generated by Django 5.1.2 on 2024-10-30 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Consumptions",
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
                (
                    "name",
                    models.CharField(
                        max_length=70, null=True, verbose_name="Промежуток расходов"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ownpr",
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
                (
                    "material",
                    models.IntegerField(null=True, verbose_name="Материальные затраты"),
                ),
                ("work", models.IntegerField(null=True, verbose_name="Оплата труда")),
                (
                    "social",
                    models.IntegerField(
                        null=True, verbose_name="Социальные мероприятия"
                    ),
                ),
                (
                    "amort",
                    models.IntegerField(null=True, verbose_name="Амортизация средств"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Others",
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
                (
                    "name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Наименование расхода"
                    ),
                ),
                (
                    "money",
                    models.IntegerField(null=True, verbose_name="Кол-во расходов"),
                ),
                (
                    "cons",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.ownpr",
                        verbose_name="Общие расходы",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subcons",
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
                ("date", models.DateTimeField(null=True, verbose_name="Время")),
                ("total", models.IntegerField(null=True, verbose_name="Потрачено")),
                (
                    "con",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.consumptions",
                        verbose_name="Промежуток",
                    ),
                ),
            ],
        ),
    ]
