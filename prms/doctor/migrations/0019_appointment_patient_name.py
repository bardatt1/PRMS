# Generated by Django 5.1.3 on 2024-12-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_alter_doctor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
