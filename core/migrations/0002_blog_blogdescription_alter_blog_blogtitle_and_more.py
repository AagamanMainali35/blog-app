# Generated by Django 5.1 on 2024-08-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='BlogDescription',
            field=models.CharField(max_length=50, null=True, verbose_name='Blogtitle'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='BlogTitle',
            field=models.CharField(max_length=50, null=True, verbose_name='Blogtitle'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Username',
            field=models.CharField(max_length=50, null=True, verbose_name='username'),
        ),
    ]
