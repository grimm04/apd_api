# Generated by Django 3.2 on 2022-03-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20220318_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='roles',
            field=models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True),
        ),
    ]
