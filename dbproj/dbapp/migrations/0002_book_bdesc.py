# Generated by Django 3.2.12 on 2023-07-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bdesc',
            field=models.TextField(default='this is book'),
            preserve_default=False,
        ),
    ]
