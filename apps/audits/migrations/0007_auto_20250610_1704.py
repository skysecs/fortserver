# Generated by Django 4.1.13 on 2025-06-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audits", "0006_alter_ftplog_account_alter_ftplog_asset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftplog',
            name='asset',
            field=models.CharField(db_index=True, max_length=768, verbose_name='Asset'),
        ),
    ]
