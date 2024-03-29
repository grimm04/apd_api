# Generated by Django 3.2 on 2022-04-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointType',
            fields=[
                ('id_pointtype', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('datum_created', models.DateTimeField(blank=True, null=True)),
                ('log_his', models.IntegerField(blank=True, null=True)),
                ('jenispoint', models.IntegerField(blank=True, null=True)),
                ('show_grafik', models.IntegerField(blank=True, null=True)),
                ('no_urut', models.IntegerField(blank=True, null=True)),
                ('warna', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('send_telegram', models.IntegerField(blank=True, null=True)),
                ('format_pesan', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100, null=True)),
                ('durasi_perubahan', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'scd_pointtype',
                'managed': False,
            },
        ),
    ]
