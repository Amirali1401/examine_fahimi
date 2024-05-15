# Generated by Django 4.2.13 on 2024-05-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoproject', '0004_rename_items_todoitems_title_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(choices=[('FINISHED', 'FINISHED'), ('IMCOMPLETED', 'IMCOMPLETED')], default=False),
        ),
    ]