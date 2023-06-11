# Generated by Django 3.2.17 on 2023-04-04 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0111_auto_20230321_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('asset_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'verbose_name': 'Custom asset',
            },
            bases=('assets.asset',),
        ),
        migrations.AddField(
            model_name='platform',
            name='custom_fields',
            field=models.JSONField(default=list, null=True, verbose_name='Custom fields'),
        ),
        migrations.AddField(
            model_name='asset',
            name='custom_info',
            field=models.JSONField(default=dict, verbose_name='Custom info'),
        ),
        migrations.AddField(
            model_name='asset',
            name='gathered_info',
            field=models.JSONField(blank=True, default=dict, verbose_name='Gathered info'),
        ),
        migrations.RemoveField(
            model_name='asset',
            name='info',
        ),
    ]
