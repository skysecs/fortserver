# Generated by Django 4.1.13 on 2024-12-05 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_integrationapplication_delete_serviceintegration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushaccountautomation',
            name='action',
        ),
        migrations.RemoveField(
            model_name='pushaccountautomation',
            name='triggers',
        ),
        migrations.RemoveField(
            model_name='pushaccountautomation',
            name='username',
        ),
    ]
