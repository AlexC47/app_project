# Generated by Django 3.1.7 on 2021-05-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0002_auto_20210506_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needtemplatemodel',
            name='tag',
            field=models.ManyToManyField(to='needs.TagModel'),
        ),
    ]
