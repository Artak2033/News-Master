# Generated by Django 3.2.4 on 2021-08-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default='Admin', max_length=30, verbose_name='Author'),
        ),
    ]