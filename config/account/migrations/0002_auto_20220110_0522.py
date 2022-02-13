# Generated by Django 3.1 on 2022-01-10 01:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default='hi there!'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='thumbnail',
            field=models.ImageField(default='1', upload_to='images'),
        ),
    ]
