# Generated by Django 3.0.7 on 2020-07-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20200704_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=200, null=True, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True, verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.IntegerField(null=True, verbose_name='성별'),
        ),
    ]
