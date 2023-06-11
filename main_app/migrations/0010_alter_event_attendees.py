# Generated by Django 4.2.2 on 2023-06-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_userprofile_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, limit_choices_to={'family': models.F('user__userprofile__family')}, to='main_app.userprofile'),
        ),
    ]
