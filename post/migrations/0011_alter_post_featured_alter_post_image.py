# Generated by Django 4.1.5 on 2023-01-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_options_alter_post_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
