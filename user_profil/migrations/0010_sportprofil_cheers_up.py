# Generated by Django 3.2.3 on 2021-06-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profil', '0009_alter_sportprofil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportprofil',
            name='cheers_up',
            field=models.IntegerField(default=0),
        ),
    ]