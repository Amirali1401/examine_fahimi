# Generated by Django 4.2.13 on 2024-05-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoproject', '0002_remove_todolist_items_todolist_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoItem',
            new_name='TodoItems',
        ),
        migrations.RenameField(
            model_name='todoitems',
            old_name='item',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='item',
            new_name='items',
        ),
    ]