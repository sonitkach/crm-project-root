# Generated by Django 3.1 on 2020-11-14 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_auto_20201114_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='speciality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.speciality'),
        ),
    ]