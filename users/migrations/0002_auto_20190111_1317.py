# Generated by Django 2.0.9 on 2019-01-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='froma',
            new_name='Home',
        ),
    ]
