# Generated by Django 4.1.13 on 2024-11-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_accountrisk_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountrisk",
            name="details",
            field=models.JSONField(default=list, verbose_name="Details"),
        ),
        migrations.AlterField(
            model_name="accountrisk",
            name="comment",
            field=models.TextField(blank=True, default="", verbose_name="Comment"),
        ),
    ]
