# Generated by Django 2.2.7 on 2021-03-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_auto_20210315_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='leavetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]