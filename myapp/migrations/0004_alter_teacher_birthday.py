# Generated by Django 4.2.7 on 2024-01-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_teacher_age_alter_teacher_birthday_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="birthday",
            field=models.DateField(default="1999-01-01", verbose_name="出生日期"),
        ),
    ]
