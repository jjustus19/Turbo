# Generated by Django 5.0.3 on 2024-04-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulingApp', '0002_remove_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
