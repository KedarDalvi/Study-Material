# Generated by Django 3.1 on 2021-06-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0025_auto_20210615_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_code',
            field=models.IntegerField(default=204192),
        ),
    ]
