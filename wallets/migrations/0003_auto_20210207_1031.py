# Generated by Django 3.1.5 on 2021-02-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_auto_20210207_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='kyc_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='wallet_address',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
