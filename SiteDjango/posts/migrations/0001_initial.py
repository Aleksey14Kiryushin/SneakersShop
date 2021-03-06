# Generated by Django 4.0.5 on 2022-07-02 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_file', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='posts.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('announcement', models.CharField(max_length=100, verbose_name='Announcement')),
                ('full_text', models.TextField(verbose_name='Full Text')),
                ('date', models.DateTimeField(verbose_name='Date of publication')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
                ('img_file', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='posts.image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
