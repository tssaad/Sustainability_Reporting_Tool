# Generated by Django 4.0 on 2021-12-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentinfo',
            name='finish_at',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
