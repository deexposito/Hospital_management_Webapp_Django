# Generated by Django 4.1 on 2023-02-05 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_condition_check_up_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patienthasdiagnosis',
            old_name='dignosis',
            new_name='diagnosis',
        ),
    ]
