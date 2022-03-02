# Generated by Django 4.0.1 on 2022-03-02 02:41

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.SmallIntegerField(blank=True, choices=[(0, '0~19'), (1, '20~29'), (2, '30~39'), (3, '40~49'), (4, '50~59'), (5, '60~69'), (6, '60~'), (7, 'please set this value')], default=7),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'male'), (1, 'female'), (2, 'other'), (4, 'please set this value')], default=4),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nationality',
            field=models.CharField(blank=True, default='please set this value', max_length=25),
        ),
    ]
