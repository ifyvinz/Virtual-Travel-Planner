# Generated by Django 4.2.6 on 2023-11-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_trip_options_remove_trip_trip_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='arrival',
            field=models.DateField(),
        ),
    ]
