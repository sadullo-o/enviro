# Generated by Django 4.1.3 on 2022-11-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_whyus'),
    ]

    operations = [
        migrations.AddField(
            model_name='whyus',
            name='klass',
            field=models.CharField(default='long_contents', max_length=200),
        ),
    ]