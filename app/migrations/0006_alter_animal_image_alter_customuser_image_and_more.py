# Generated by Django 5.1.1 on 2024-09-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_categorypost_mentor_university_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/animals'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='media/users/default.png', upload_to='media/users'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/posts'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/shelters'),
        ),
    ]
