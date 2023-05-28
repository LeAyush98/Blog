# Generated by Django 4.2.1 on 2023-05-28 17:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("author", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=200)),
                ("subtitle", models.CharField(max_length=400)),
                ("date", models.CharField(max_length=30)),
                ("body", ckeditor.fields.RichTextField()),
                ("img_url", models.URLField()),
            ],
        ),
    ]
