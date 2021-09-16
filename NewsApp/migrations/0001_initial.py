# Generated by Django 3.2.4 on 2021-08-11 16:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category title')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Article title')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='NewsPhoto', verbose_name='Photo')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='News Content')),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='published', max_length=10, verbose_name='Status')),
                ('author', models.CharField(default='One planet', max_length=30, verbose_name='Author')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('additional_category', models.ManyToManyField(blank=True, related_name='Additional', to='NewsApp.Category', verbose_name='Additional_categories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsApp.category')),
            ],
        ),
    ]