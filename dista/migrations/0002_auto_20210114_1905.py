# Generated by Django 3.1.5 on 2021-01-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dista', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': '댓글들', 'verbose_name_plural': '댓글'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',), 'verbose_name': '글들', 'verbose_name_plural': '글'},
        ),
    ]
