# Generated by Django 4.0 on 2022-01-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='promote',
            field=models.BooleanField(default=False),
        ),
    ]
