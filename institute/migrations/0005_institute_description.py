# Generated by Django 4.0 on 2021-12-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_institute_img_alter_institute_business_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
