# Generated by Django 3.1.7 on 2021-05-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210513_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='body3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='body4',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
