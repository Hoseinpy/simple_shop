# Generated by Django 5.0.7 on 2024-08-06 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='text',
        ),
    ]
