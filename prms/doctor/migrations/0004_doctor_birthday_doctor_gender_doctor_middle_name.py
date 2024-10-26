# Generated by Django 5.1.1 on 2024-10-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_patient_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
