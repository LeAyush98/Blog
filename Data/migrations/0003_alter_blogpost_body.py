# Generated by Django 4.2.1 on 2023-05-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Data", "0002_alter_blogpost_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="body",
            field=models.CharField(max_length=2000),
        ),
    ]
