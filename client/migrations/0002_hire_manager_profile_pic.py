# Generated by Django 3.0.6 on 2020-08-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire_manager',
            name='profile_pic',
            field=models.ImageField(default='apps.png', upload_to=''),
        ),
    ]
