# Generated by Django 3.0.9 on 2021-03-07 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpayment',
            old_name='email',
            new_name='email_address',
        ),
    ]