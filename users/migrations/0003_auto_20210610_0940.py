# Generated by Django 3.1.7 on 2021-06-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210607_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='profiles'),
        ),
    ]
