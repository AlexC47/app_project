# Generated by Django 3.1.7 on 2021-06-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210615_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Cluj-Napoca', max_length=255, null=True),
        ),
    ]