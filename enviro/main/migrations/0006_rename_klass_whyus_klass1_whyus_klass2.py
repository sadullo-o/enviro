# Generated by Django 4.1.3 on 2022-11-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_whyus_klass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whyus',
            old_name='klass',
            new_name='klass1',
        ),
        migrations.AddField(
            model_name='whyus',
            name='klass2',
            field=models.CharField(default='Why_us_content1', max_length=200),
        ),
    ]
