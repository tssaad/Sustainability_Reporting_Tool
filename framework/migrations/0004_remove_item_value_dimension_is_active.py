# Generated by Django 4.0 on 2021-12-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_alter_dimension_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='value',
        ),
        migrations.AddField(
            model_name='dimension',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
