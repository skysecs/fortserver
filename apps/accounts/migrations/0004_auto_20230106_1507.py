# Generated by Django 3.2.16 on 2023-01-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_automation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changesecretautomation',
            name='secret_strategy',
            field=models.CharField(choices=[('specific', 'Specific secret'), ('random', 'Random generate')], default='specific', max_length=16, verbose_name='Secret strategy'),
        ),
        migrations.AlterField(
            model_name='pushaccountautomation',
            name='secret_strategy',
            field=models.CharField(choices=[('specific', 'Specific secret'), ('random', 'Random generate')], default='specific', max_length=16, verbose_name='Secret strategy'),
        ),
    ]
