# Generated by Django 3.1.5 on 2021-01-14 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dista', '0004_auto_20210114_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dista.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='hash_tag',
            field=models.CharField(help_text='해쉬태그는 #를 따로 쓰지마세요 공백으로 자동구분 됩니다.', max_length=30),
        ),
    ]
