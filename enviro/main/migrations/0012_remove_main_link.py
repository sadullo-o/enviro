# Generated by Django 4.1.3 on 2022-11-18 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_sitecontac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='link',
        ),
    ]
