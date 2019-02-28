# Generated by Django 2.1.7 on 2019-02-24 13:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('depth', models.IntegerField(default=0)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='businesspost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='businesspost',
            name='notice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='businesspost',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='businesscomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='business.BusinessPost'),
        ),
    ]
