# Generated by Django 3.2 on 2021-05-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chalan', '0002_alter_challan_licensenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='vehicletype',
            field=models.CharField(choices=[('Car', 'Car'), ('Motercycle', 'Motercycle'), ('Bus', 'Bus'), ('Van', 'Van'), ('Truck', 'Truck')], max_length=200, null=True),
        ),
    ]
