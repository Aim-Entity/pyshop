# Generated by Django 2.2.7 on 2020-04-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200414_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='batch',
            field=models.IntegerField(default=0),
        ),
    ]
