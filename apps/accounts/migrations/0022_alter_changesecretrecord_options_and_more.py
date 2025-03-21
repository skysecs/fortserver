# Generated by Django 4.1.13 on 2024-12-09 03:15

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_pushaccountautomation_action_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changesecretrecord',
            options={'permissions': [('view_pushsecretrecord', 'Can view change secret execution'), ('add_pushsecretexecution', 'Can add change secret execution')], 'verbose_name': 'Change secret record'},
        ),
        migrations.AlterField(
            model_name='integrationapplication',
            name='logo',
            field=private_storage.fields.PrivateImageField(max_length=128, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='images', verbose_name='Logo'),
        ),
    ]
