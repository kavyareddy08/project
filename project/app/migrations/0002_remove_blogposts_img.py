# Generated by Django 3.1.1 on 2020-10-23 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogposts',
            name='img',
        ),
    ]
