# Generated by Django 2.1.5 on 2019-01-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='importance',
            field=models.BooleanField(default=False),
        ),
    ]
