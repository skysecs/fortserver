# Generated by Django 4.1.13 on 2024-11-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assets", "0008_automationexecution_result_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="automationexecution",
            name="duration",
            field=models.FloatField(default=0, verbose_name="Duration"),
        ),
    ]
