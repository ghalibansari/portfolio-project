# Generated by Django 2.0.2 on 2018-08-06 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summery',
            new_name='summary',
        ),
    ]
