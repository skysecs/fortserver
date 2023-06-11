# Generated by Django 3.2.14 on 2022-12-28 07:29

import common.db.encoder
import common.db.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0098_auto_20220430_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('connectivity', models.CharField(choices=[('-', 'Unknown'), ('ok', 'Ok'), ('err', 'Error')], default='-', max_length=16, verbose_name='Connectivity')),
                ('date_verified', models.DateTimeField(null=True, verbose_name='Date verified')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('username', models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Username')),
                ('secret_type', models.CharField(
                    choices=[('password', 'Password'), ('ssh_key', 'SSH key'), ('access_key', 'Access key'),
                             ('token', 'Token')], default='password', max_length=16, verbose_name='Secret type')),
                ('secret', common.db.fields.EncryptTextField(blank=True, null=True, verbose_name='Secret')),
                ('privileged', models.BooleanField(default=False, verbose_name='Privileged')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('version', models.IntegerField(default=0, verbose_name='Version')),
                ('source', models.CharField(default='local', max_length=30, verbose_name='Source')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts',
                                            to='assets.asset', verbose_name='Asset')),
                ('su_from',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='su_to',
                                   to='accounts.account', verbose_name='Su from')),
            ],
            options={
                'verbose_name': 'Account',
                'permissions': [('view_accountsecret', 'Can view asset account secret'),
                                ('view_historyaccount', 'Can view asset history account'),
                                ('view_historyaccountsecret', 'Can view asset history account secret')],
                'unique_together': {('username', 'asset', 'secret_type'), ('name', 'asset')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('secret_type', models.CharField(
                    choices=[('password', 'Password'), ('ssh_key', 'SSH key'), ('access_key', 'Access key'),
                             ('token', 'Token')], default='password', max_length=16, verbose_name='Secret type')),
                ('secret', common.db.fields.EncryptTextField(blank=True, null=True, verbose_name='Secret')),
                ('version', models.IntegerField(default=0, verbose_name='Version')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Account',
                'verbose_name_plural': 'historical Accounts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='AccountTemplate',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('username', models.CharField(blank=True, db_index=True, max_length=128, verbose_name='Username')),
                ('secret_type', models.CharField(
                    choices=[('password', 'Password'), ('ssh_key', 'SSH key'), ('access_key', 'Access key'),
                             ('token', 'Token')], default='password', max_length=16, verbose_name='Secret type')),
                ('secret', common.db.fields.EncryptTextField(blank=True, null=True, verbose_name='Secret')),
                ('privileged', models.BooleanField(default=False, verbose_name='Privileged')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Account template',
                'permissions': [('view_accounttemplatesecret', 'Can view asset account template secret'),
                                ('change_accounttemplatesecret', 'Can change asset account template secret')],
                'unique_together': {('name', 'org_id')},
            },
        ),
    ]
