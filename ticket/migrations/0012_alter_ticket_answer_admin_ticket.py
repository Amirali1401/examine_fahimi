# Generated by Django 4.2.13 on 2024-05-15 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_ticket_answer_admin_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='answer_admin_ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_admin_tickets', to='ticket.answeradmin'),
        ),
    ]