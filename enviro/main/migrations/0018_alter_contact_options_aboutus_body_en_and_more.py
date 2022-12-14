# Generated by Django 4.1.3 on 2022-11-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_rename_p_name_orders_p_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='body_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='body_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='body_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_1_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_1_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_1_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_2_en',
            field=models.CharField(default='aa', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_2_ru',
            field=models.CharField(default='aa', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='body_2_uz',
            field=models.CharField(default='aa', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_1_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_1_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_1_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_2_en',
            field=models.CharField(default='ss', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_2_ru',
            field=models.CharField(default='ss', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='oav',
            name='title_2_uz',
            field=models.CharField(default='ss', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='body_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='body_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='body_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productitems',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='body_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='body_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='body_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='body_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='body_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='body_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
