# Generated by Django 4.1.13 on 2024-12-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_sshkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontoken',
            name='face_monitor_token',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Face monitor token'),
        ),
    ]