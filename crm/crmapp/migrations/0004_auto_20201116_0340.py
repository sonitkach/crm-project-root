# Generated by Django 3.1 on 2020-11-16 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crmapp', '0003_auto_20201114_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='friends',
            field=models.ManyToManyField(related_name='_company_friends_+', to='crmapp.Company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]