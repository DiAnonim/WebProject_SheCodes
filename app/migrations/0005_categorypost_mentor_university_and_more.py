# Generated by Django 5.1.1 on 2024-09-14 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customuser_isstudent_alter_customuser_image_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CategoryPost',
                'verbose_name_plural': 'CategoryPos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/mentor')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('typeOfActivity', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentors',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/university')),
                ('name', models.TextField()),
                ('website', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
                'ordering': ['-created_at'],
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryAnimal',
        ),
        migrations.AlterModelOptions(
            name='categoryanimal',
            options={'ordering': ['-created_at'], 'verbose_name': 'CategoryAnimal', 'verbose_name_plural': 'CategoryAnimals'},
        ),
        migrations.AddField(
            model_name='animal',
            name='categoryPost',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.categorypost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.categorypost'),
        ),
    ]
