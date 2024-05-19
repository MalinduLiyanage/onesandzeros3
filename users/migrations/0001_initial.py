# Generated by Django 5.0.6 on 2024-05-18 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('profile_picture', models.CharField(blank=True, max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
                ('activation_link', models.CharField(blank=True, max_length=255)),
                ('activation_status', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='users.user')),
            ],
        ),
    ]