# Generated by Django 2.2.7 on 2020-04-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200414_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='batch',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
