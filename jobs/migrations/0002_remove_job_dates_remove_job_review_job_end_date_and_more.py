# Generated by Django 4.2.13 on 2024-07-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='job',
            name='review',
        ),
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateField(default='2024-20-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateField(default='2024-01-03'),
            preserve_default=False,
        ),
    ]