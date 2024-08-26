# Generated by Django 5.1 on 2024-08-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blog_blogdescription_alter_blog_blogtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BlogDescription',
            field=models.CharField(max_length=50, null=True, verbose_name='BlogDesc'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='CoreImages'),
        ),
    ]
