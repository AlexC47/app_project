# Generated by Django 3.1.7 on 2021-06-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0006_delete_userneedpending'),
    ]

    operations = [
        migrations.AddField(
            model_name='userneedmodel',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
