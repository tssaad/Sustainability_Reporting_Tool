# Generated by Django 4.0 on 2021-12-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0006_alter_webassessmentinfo_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webassessmentinfo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='webassessmentinfo',
            name='finish_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
