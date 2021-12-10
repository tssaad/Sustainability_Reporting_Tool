# Generated by Django 4.0 on 2021-12-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_city_options_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('Europe', 'Europe'), ('Africa', 'Africa'), ('North America', 'North America'), ('South America', 'South America'), ('Asia', 'Asia'), ('Australia', 'Australia')], max_length=225),
        ),
    ]