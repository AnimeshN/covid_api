# Generated by Django 3.0.5 on 2020-07-24 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200723_1309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CovidHospbeds',
            new_name='Hospbeds',
        ),
    ]
