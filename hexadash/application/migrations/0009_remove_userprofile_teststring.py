# Generated by Django 4.0.5 on 2024-06-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_remove_userprofile_image_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='testString',
        ),
    ]
