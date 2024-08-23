# Generated by Django 5.1 on 2024-08-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_alter_trips_options_trips_image_trips_price_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                    "data",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="image/", verbose_name="фото блога"),
                ),
                (
                    "title",
                    models.CharField(max_length=20, verbose_name="заголовок блога"),
                ),
            ],
            options={
                "verbose_name": "",
                "verbose_name_plural": "блог",
            },
        ),
    ]
