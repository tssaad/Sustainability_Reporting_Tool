# Generated by Django 4.0 on 2021-12-08 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_city_options_alter_country_options'),
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='settings.city'),
            preserve_default=False,
        ),
    ]
