# Generated by Django 3.1.5 on 2021-02-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='controller_nickname',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='creation_dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
