# Generated by Django 3.1 on 2021-06-15 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0028_auto_20210615_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnotes',
            name='uploaded_on',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='laboratory_videos',
            name='uploaded_on',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='video_lectures',
            name='uploaded_on',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
