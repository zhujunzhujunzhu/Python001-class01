# Generated by Django 2.2 on 2020-08-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_user_name',
            field=models.CharField(default='', max_length=256, verbose_name='用户'),
        ),
    ]
