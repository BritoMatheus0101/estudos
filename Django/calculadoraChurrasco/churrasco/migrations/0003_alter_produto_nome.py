# Generated by Django 3.2.4 on 2021-07-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churrasco', '0002_auto_20210706_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome'),
        ),
    ]
