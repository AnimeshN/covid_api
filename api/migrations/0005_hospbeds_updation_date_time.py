# Generated by Django 3.0.5 on 2020-07-31 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200724_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospbeds',
            name='updation_date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='date_published'),
        ),
    ]