# Generated by Django 3.1.3 on 2021-04-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]