# Generated by Django 3.1.5 on 2021-01-14 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dista', '0006_auto_20210115_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='post',
            name='following',
        ),
    ]
