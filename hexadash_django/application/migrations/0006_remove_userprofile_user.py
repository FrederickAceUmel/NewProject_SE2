# Generated by Django 5.0.6 on 2024-06-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]