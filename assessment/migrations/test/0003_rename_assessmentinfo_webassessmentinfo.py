# Generated by Django 4.0 on 2021-12-13 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0009_alter_institutetype_name_alter_specialty_name'),
        ('authentication', '0004_user_img'),
        ('assessment', '0002_alter_assessmentinfo_finish_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssessmentInfo',
            new_name='WebAssessmentInfo',
        ),
    ]