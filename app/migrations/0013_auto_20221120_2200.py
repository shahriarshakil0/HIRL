# Generated by Django 3.0.5 on 2022-11-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_members_m_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='m_post',
            field=models.CharField(choices=[('LD', 'LAB_DIRECTOR'), ('LA', 'LAB_ADVISOR'), ('RC', 'RESEARCH_COORDINATOR'), ('R', 'RESEARCHER'), ('LM', 'LAB_MEMBER')], default='LM', max_length=2),
        ),
    ]
