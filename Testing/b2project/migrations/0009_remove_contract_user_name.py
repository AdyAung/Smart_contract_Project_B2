# Generated by Django 3.2.6 on 2021-09-07 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2project', '0008_contract_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='user_name',
        ),
    ]