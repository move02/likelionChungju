# Generated by Django 2.1.5 on 2019-01-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_post_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
