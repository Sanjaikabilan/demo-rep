# Generated by Django 4.1.7 on 2023-03-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("graphe", "0002_rename_data_sensordata_accel_sensordata_disp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sensordata",
            name="accel",
        ),
        migrations.RemoveField(
            model_name="sensordata",
            name="disp",
        ),
        migrations.AddField(
            model_name="sensordata",
            name="data",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
