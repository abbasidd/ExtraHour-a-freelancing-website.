# Generated by Django 3.0.6 on 2020-08-11 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('freelancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complexity_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Expected_duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('payment_amount', models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True)),
                ('complexity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.Complexity')),
                ('expected_duration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.Expected_duration')),
                ('hire_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Hire_manager')),
                ('main_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Skill')),
                ('payment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='freelancer.Payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Other_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.Skill')),
            ],
        ),
    ]
