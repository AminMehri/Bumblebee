# Generated by Django 3.1 on 2022-01-03 00:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_promote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]