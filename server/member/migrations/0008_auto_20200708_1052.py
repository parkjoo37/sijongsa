# Generated by Django 3.0.7 on 2020-07-08 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20200708_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=200, verbose_name='주소'),
        ),
    ]
