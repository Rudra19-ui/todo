# Generated by Django 5.1 on 2025-03-09 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
