# Generated by Django 3.2.3 on 2021-07-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20210719_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='trainingDateMonthNb',
            field=models.CharField(default='', max_length=20),
        ),
    ]
