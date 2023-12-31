# Generated by Django 3.2.16 on 2023-02-07 04:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0108_alter_platform_charset'),
        ('accounts', '0005_alter_changesecretrecord_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatheredAccount',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('present', models.BooleanField(default=True, verbose_name='Present')),
                ('date_last_login', models.DateTimeField(null=True, verbose_name='Date last login')),
                ('username', models.CharField(blank=True, db_index=True, max_length=32, verbose_name='Username')),
                ('address_last_login', models.CharField(default='', max_length=39, verbose_name='Address last login')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.asset', verbose_name='Asset')),
            ],
            options={
                'verbose_name': 'Gather account',
                'ordering': ['asset'],
                'unique_together': {('username', 'asset')},
            },
        ),
    ]
