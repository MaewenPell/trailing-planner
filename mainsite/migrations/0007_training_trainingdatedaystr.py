# Generated by Django 3.2.3 on 2021-06-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_training_trainingdateweeknb'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='trainingDateDayStr',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
