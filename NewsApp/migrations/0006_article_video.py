# Generated by Django 3.2.4 on 2021-09-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='NewsVideos', verbose_name='Video'),
        ),
    ]
