# Generated by Django 3.1.7 on 2021-05-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210514_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
