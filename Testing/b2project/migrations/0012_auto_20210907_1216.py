# Generated by Django 3.2.6 on 2021-09-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2project', '0011_auto_20210907_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='EndDate',
            field=models.DateTimeField(max_length=8, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='StartDate',
            field=models.DateTimeField(max_length=8, verbose_name='Start Date'),
        ),
    ]