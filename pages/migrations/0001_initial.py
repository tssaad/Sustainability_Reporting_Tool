# Generated by Django 4.0 on 2021-12-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='pages/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
