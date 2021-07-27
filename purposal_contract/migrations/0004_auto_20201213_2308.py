# Generated by Django 3.0.6 on 2020-12-13 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purposal_contract', '0003_auto_20200929_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purposal_contract.Message')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='freelancer_recipient',
            name='freelancer',
        ),
        migrations.RemoveField(
            model_name='freelancer_recipient',
            name='message',
        ),
        migrations.DeleteModel(
            name='client_recipient',
        ),
        migrations.DeleteModel(
            name='freelancer_recipient',
        ),
    ]