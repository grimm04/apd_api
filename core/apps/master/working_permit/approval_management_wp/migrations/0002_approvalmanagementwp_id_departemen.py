# Generated by Django 3.2 on 2022-04-23 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departemen', '0001_initial'),
        ('approval_management_wp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvalmanagementwp',
            name='id_departemen',
            field=models.ForeignKey(blank=True, db_column='id_departemen', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='departemen.departemen'),
        ),
    ]
