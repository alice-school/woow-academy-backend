# Generated by Django 5.0.1 on 2024-02-27 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_alter_cv_profile_about"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cv_profile",
            name="about",
            field=models.TimeField(),
        ),
    ]
