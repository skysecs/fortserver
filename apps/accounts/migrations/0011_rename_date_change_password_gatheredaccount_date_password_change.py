# Generated by Django 4.1.13 on 2024-11-12 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_accountrisk_details_alter_accountrisk_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gatheredaccount",
            old_name="date_change_password",
            new_name="date_password_change",
        ),
    ]
