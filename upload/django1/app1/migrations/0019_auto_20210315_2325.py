# Generated by Django 2.2.7 on 2021-03-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20210311_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='allnum',
        ),
        migrations.RemoveField(
            model_name='status',
            name='seatednum',
        ),
        migrations.AddField(
            model_name='status',
            name='orilat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='orilon',
            field=models.FloatField(default=0.0),
        ),
    ]