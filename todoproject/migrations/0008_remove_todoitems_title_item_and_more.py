# Generated by Django 4.2.13 on 2024-05-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoproject', '0007_alter_todolist_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitems',
            name='title_item',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='completed',
        ),
        migrations.AddField(
            model_name='todoitems',
            name='completed',
            field=models.CharField(choices=[('Finished', 'Finished'), ('Imcompleted', 'Imcompleted')], default='Imcompleted', max_length=20),
        ),
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
