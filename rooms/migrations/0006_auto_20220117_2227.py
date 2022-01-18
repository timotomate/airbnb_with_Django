# Generated by Django 2.2.5 on 2022-01-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220117_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='houserule',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]