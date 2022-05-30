# Generated by Django 4.0.4 on 2022-05-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('staff', 'staff'), ('client', 'client')], max_length=20, null=True),
        ),
    ]