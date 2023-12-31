# Generated by Django 3.2.19 on 2023-07-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('coursename', models.CharField(max_length=20)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=25)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='course/cover/')),
                ('course_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
