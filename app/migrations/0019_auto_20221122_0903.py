# Generated by Django 3.0.5 on 2022-11-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_publication_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentresearch',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
