# Generated by Django 4.0 on 2021-12-08 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_delete_continent_country_continent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
