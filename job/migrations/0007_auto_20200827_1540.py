# Generated by Django 3.0.6 on 2020-08-27 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0001_initial'),
        ('job', '0006_auto_20200826_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='main_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Skill'),
        ),
    ]