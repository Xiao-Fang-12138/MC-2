# Generated by Django 2.2.7 on 2021-01-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alertlog_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cardid',
            field=models.IntegerField(default=-1),
        ),
    ]