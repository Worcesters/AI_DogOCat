# Generated by Django 4.0.4 on 2022-06-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='result',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
