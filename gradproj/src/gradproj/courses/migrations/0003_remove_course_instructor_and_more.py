# Generated by Django 4.0.3 on 2022-03-20 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='numberofVedioes',
        ),
    ]
