# Generated by Django 3.0.5 on 2022-11-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_members_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='img',
            field=models.ImageField(null=True, upload_to='img/%y'),
        ),
    ]
