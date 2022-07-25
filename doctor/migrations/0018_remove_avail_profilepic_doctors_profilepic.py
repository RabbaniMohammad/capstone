# Generated by Django 4.0.6 on 2022-07-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_avail_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avail',
            name='profilepic',
        ),
        migrations.AddField(
            model_name='doctors',
            name='profilepic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
