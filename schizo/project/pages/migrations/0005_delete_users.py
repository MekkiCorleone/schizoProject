# Generated by Django 4.2.1 on 2023-05-22 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_delete_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
