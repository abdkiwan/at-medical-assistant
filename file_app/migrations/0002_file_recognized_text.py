# Generated by Django 2.0.5 on 2018-12-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='recognized_text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
