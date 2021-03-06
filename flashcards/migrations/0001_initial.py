# Generated by Django 3.0.7 on 2020-06-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='FlashCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flash_title', models.CharField(max_length=40)),
                ('flash_course', models.CharField(max_length=40)),
                ('flash_body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
