# Generated by Django 4.1.13 on 2024-11-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assets", "0007_baseautomation_start_time"),
        ("accounts", "0008_remove_accountrisk_confirmed_accountrisk_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gatheredaccount",
            name="date_change_password",
            field=models.DateTimeField(null=True, verbose_name="Date change password"),
        ),
        migrations.AddField(
            model_name="gatheredaccount",
            name="date_password_expired",
            field=models.DateTimeField(null=True, verbose_name="Date password expired"),
        ),
        migrations.AlterField(
            model_name="accountrisk",
            name="comment",
            field=models.TextField(default="", verbose_name="Comment"),
        ),
        migrations.AlterField(
            model_name="accountrisk",
            name="risk",
            field=models.CharField(
                choices=[
                    ("zombie", "Long time no login"),
                    ("ghost", "Not managed"),
                    ("groups_changed", "Groups change"),
                    ("sudoers_changed", "Sudo changed"),
                    ("authorized_keys_changed", "Authorized keys changed"),
                    ("account_deleted", "Account delete"),
                    ("password_expired", "Password expired"),
                    ("long_time_password", "Long time no change"),
                    ("weak_password", "Weak password"),
                    ("password_error", "Password error"),
                    ("no_admin_account", "No admin account"),
                    ("others", "Others"),
                ],
                max_length=128,
                verbose_name="Risk",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="accountrisk",
            unique_together={("asset", "username", "risk")},
        ),
        migrations.DeleteModel(
            name="GatheredAccountDiff",
        ),
    ]
