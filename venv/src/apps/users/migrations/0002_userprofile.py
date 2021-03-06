# Generated by Django 3.1 on 2020-08-26 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
