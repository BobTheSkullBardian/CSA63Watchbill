# Generated by Django 3.1.3 on 2021-01-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
