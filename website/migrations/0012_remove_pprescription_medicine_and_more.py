# Generated by Django 5.0.4 on 2024-09-07 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_rename_prescription_pprescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pprescription',
            name='medicine',
        ),
        migrations.AddField(
            model_name='pprescription',
            name='medicinename',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.medicine'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pprescription',
            name='patientname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.patient'),
        ),
    ]