# Generated by Django 2.0.9 on 2018-12-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0006_comment_comment_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pics',
            field=models.FileField(blank=True, upload_to='post_pics'),
        ),
    ]
