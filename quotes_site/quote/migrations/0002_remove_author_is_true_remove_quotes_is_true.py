# Generated by Django 4.2.3 on 2023-07-15 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='is_true',
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='is_true',
        ),
    ]
