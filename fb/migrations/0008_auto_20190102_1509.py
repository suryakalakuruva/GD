# Generated by Django 2.0.9 on 2019-01-02 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0007_auto_20181229_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_pic',
        ),
    ]