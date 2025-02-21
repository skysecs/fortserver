# Generated by Django 4.1.13 on 2024-11-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ops", "0004_historicaljob_start_time_job_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaljob",
            name="crontab",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Crontab"
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="crontab",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Crontab"
            ),
        ),
    ]
