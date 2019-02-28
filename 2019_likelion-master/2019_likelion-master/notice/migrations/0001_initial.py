# Generated by Django 2.1.5 on 2019-01-29 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
