# Generated by Django 3.0.5 on 2022-11-16 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221116_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentresearch',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='members',
            name='cap',
        ),
    ]
