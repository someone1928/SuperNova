# Generated by Django 3.1.3 on 2021-04-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210425_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_image'),
        ),
    ]
