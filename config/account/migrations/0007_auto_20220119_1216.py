# Generated by Django 3.1 on 2022-01-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220117_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='thumbnail',
            field=models.ImageField(blank=True, default='../static/images/avatars/user-05.jpeg', upload_to='images'),
        ),
    ]
