# Generated by Django 3.1 on 2021-06-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0027_auto_20210615_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='classnotes',
            name='uploaded_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='laboratory_videos',
            name='uploaded_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='video_lectures',
            name='uploaded_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
