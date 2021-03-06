# Generated by Django 3.1.7 on 2021-04-05 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20210331_0750"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="status",
            field=models.TextField(
                choices=[
                    ("DRAFT", "Draft"),
                    ("EDITING", "Editing"),
                    ("PUBLISHED", "Published"),
                    ("REJECTED", "Rejected"),
                ],
                default="DRAFT",
                verbose_name="Status",
            ),
        ),
    ]
