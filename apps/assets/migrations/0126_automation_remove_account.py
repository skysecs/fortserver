# Generated by Django 4.1.10 on 2023-12-05 10:03
from functools import reduce

from django.db import migrations, models
from django.db.models import F


def migrate_automation_ansible_remove_account(apps, *args):
    automation_model = apps.get_model('assets', 'PlatformAutomation')
    automation_map = {
        ('oracle',): 'remove_account_oracle',
        ('windows',): 'remove_account_windows',
        ('mongodb',): 'remove_account_mongodb',
        ('linux', 'unix'): 'remove_account_posix',
        ('sqlserver',): 'remove_account_sqlserver',
        ('mysql', 'mariadb'): 'remove_account_mysql',
        ('postgresql',): 'remove_account_postgresql',
    }

    update_objs = []
    types = list(reduce(lambda x, y: x + y, automation_map.keys()))
    qs = automation_model.objects.filter(platform__type__in=types).annotate(tp=F('platform__type'))
    for automation in qs:
        for types, method in automation_map.items():
            if automation.tp in types:
                automation.remove_account_enabled = True
                automation.remove_account_method = method
                break
        update_objs.append(automation)
    automation_model.objects.bulk_update(update_objs, ['remove_account_enabled', 'remove_account_method'])


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0125_auto_20231011_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformautomation',
            name='remove_account_enabled',
            field=models.BooleanField(default=False, verbose_name='Remove account enabled'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='remove_account_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Remove account method'),
        ),
        migrations.AddField(
            model_name='platformautomation',
            name='remove_account_params',
            field=models.JSONField(default=dict, verbose_name='Remove account params'),
        ),
        migrations.RunPython(migrate_automation_ansible_remove_account)
    ]
