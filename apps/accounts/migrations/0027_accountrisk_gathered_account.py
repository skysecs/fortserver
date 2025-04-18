# Generated by Django 4.1.13 on 2025-01-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0026_accountrisk_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountrisk",
            name="gathered_account",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="risks",
                to="accounts.gatheredaccount",
            ),
        ),
    ]
