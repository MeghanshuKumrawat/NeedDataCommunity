# Generated by Django 4.2.3 on 2023-07-30 12:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_course_coursekeypoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
