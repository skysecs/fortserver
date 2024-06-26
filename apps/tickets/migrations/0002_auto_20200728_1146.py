# Generated by Django 4.1.13 on 2024-05-09 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acls', '0002_auto_20210926_1047'),
        ('terminal', '0002_auto_20171228_0025'),
        ('tickets', '0001_initial'),
        ('assets', '0002_auto_20180105_1807'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketassignee',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assignees', to=settings.AUTH_USER_MODEL, verbose_name='Assignee'),
        ),
        migrations.AddField(
            model_name='ticketassignee',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assignees', to='tickets.ticketstep'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied_tickets', to=settings.AUTH_USER_MODEL, verbose_name='Applicant'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='flow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='tickets.ticketflow', verbose_name='TicketFlow'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.ticket'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='approvalrule',
            name='assignees',
            field=models.ManyToManyField(related_name='assigned_ticket_flow_approval_rule', to=settings.AUTH_USER_MODEL, verbose_name='Assignees'),
        ),
        migrations.CreateModel(
            name='SuperTicket',
            fields=[
            ],
            options={
                'verbose_name': 'Super ticket',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('tickets.ticket',),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('serial_num',)},
        ),
        migrations.AddField(
            model_name='applyloginassetticket',
            name='apply_login_asset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.asset', verbose_name='Login asset'),
        ),
        migrations.AddField(
            model_name='applyloginassetticket',
            name='apply_login_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Login user'),
        ),
        migrations.AddField(
            model_name='applycommandticket',
            name='apply_from_cmd_filter_acl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acls.commandfilteracl', verbose_name='Command filter acl'),
        ),
        migrations.AddField(
            model_name='applycommandticket',
            name='apply_from_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='terminal.session', verbose_name='Session'),
        ),
        migrations.AddField(
            model_name='applycommandticket',
            name='apply_run_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Run user'),
        ),
        migrations.AddField(
            model_name='applyassetticket',
            name='apply_assets',
            field=models.ManyToManyField(to='assets.asset', verbose_name='Asset'),
        ),
        migrations.AddField(
            model_name='applyassetticket',
            name='apply_nodes',
            field=models.ManyToManyField(to='assets.node', verbose_name='Node'),
        ),
    ]
