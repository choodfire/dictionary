# Generated by Django 4.1.5 on 2023-01-16 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('releaseDate', models.DateTimeField(default=datetime.datetime(2023, 1, 16, 19, 29, 2, 34280, tzinfo=datetime.timezone.utc))),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
