# Generated by Django 5.0.3 on 2024-04-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulingApp', '0002_rename_user_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Supervisor', 'Supervisor'), ('Instructor', 'Instructor'), ('TA', 'Ta')], default='TA', max_length=20),
        ),
    ]
