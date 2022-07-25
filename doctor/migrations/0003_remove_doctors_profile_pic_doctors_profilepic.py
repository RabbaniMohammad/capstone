# Generated by Django 4.0.6 on 2022-07-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctors_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='doctors',
            name='profilepic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]