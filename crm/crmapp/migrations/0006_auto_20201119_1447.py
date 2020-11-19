# Generated by Django 3.1 on 2020-11-19 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0005_auto_20201117_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='friends',
            field=models.ManyToManyField(related_name='_company_friends_+', through='crmapp.Friendship', to='crmapp.Company'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frinedship_receiver', to='crmapp.company'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_sender', to='crmapp.company'),
        ),
    ]