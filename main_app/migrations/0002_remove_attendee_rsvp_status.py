# Generated by Django 4.2.1 on 2023-06-10 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='rsvp_status',
        ),
    ]