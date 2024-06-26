# Generated by Django 4.2.13 on 2024-05-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_cart', models.PositiveIntegerField(max_length=30)),
                ('number_account_cart', models.PositiveIntegerField(max_length=30)),
                ('number_shabaa_cart', models.PositiveIntegerField(max_length=50)),
                ('cvv2', models.PositiveSmallIntegerField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='user.first_name', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='user.last_name', max_length=200),
        ),
    ]
