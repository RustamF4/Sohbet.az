# Generated by Django 4.2.11 on 2024-04-24 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='media/uploads/profile_pictures/default.png', upload_to='media/uploads/profile_pictures')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
