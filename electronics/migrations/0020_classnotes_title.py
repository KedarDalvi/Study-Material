# Generated by Django 3.1 on 2021-06-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0019_auto_20210614_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='classnotes',
            name='title',
            field=models.CharField(default='Aneesh Berde', max_length=100),
        ),
    ]
