# Generated by Django 4.1.13 on 2024-11-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_remove_accountrisk_account_accountrisk_asset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountrisk",
            name="risk",
            field=models.CharField(
                choices=[
                    ('zombie', 'Long time no login'),
                    ('ghost', 'Not managed'),
                    ('long_time_password', 'Long time no change'),
                    ('weak_password', 'Weak password'),
                    ('password_error', 'Password error'),
                    ('password_expired', 'Password expired'),
                    ('group_changed', 'Group change'),
                    ('sudo_changed', 'Sudo changed'),
                    ('account_deleted', 'Account delete'),
                    ('no_admin_account', 'No admin account'),
                    ('others', 'Others')
                ],
                max_length=128,
                verbose_name="Risk",
            ),
        ),
    ]
