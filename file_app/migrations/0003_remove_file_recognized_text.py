# Generated by Django 2.0.5 on 2018-12-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_file_recognized_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='recognized_text',
        ),
    ]
