# Generated by Django 4.1.13 on 2025-04-03 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assets", "0015_automationexecution_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="DirectoryService",
            fields=[
                (
                    "asset_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="assets.asset",
                    ),
                ),
                (
                    "domain_name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=128,
                        verbose_name="Domain name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Directory service",
                "default_related_name": "ds"
            },
            bases=("assets.asset",),
        ),
        migrations.AddField(
            model_name="platform",
            name="ds_enabled",
            field=models.BooleanField(default=False, verbose_name="DS enabled"),
        ),
        migrations.AddField(
            model_name="asset",
            name="directory_services",
            field=models.ManyToManyField(
                related_name="assets",
                to="assets.directoryservice",
                verbose_name="Directory service",
            )
        ),
    ]
