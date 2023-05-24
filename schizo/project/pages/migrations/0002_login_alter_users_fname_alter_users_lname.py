# Generated by Django 4.2.1 on 2023-05-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='Fname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Lname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
