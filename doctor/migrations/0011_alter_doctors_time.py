# Generated by Django 4.0.6 on 2022-07-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_alter_doctors_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='time',
            field=models.CharField(blank=True, default='{"10AM - 11AM": "10AM - 11AM", "11AM - 12PM": "11AM TO 12PM", "12PM - 1PM": "12PM - 1PM", "2PM - 3PM": "2PM - 3PM", "3PM - 4PM": "3PM - 4PM"}', max_length=300, null=True),
        ),
    ]
