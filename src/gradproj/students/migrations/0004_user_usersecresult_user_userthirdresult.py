# Generated by Django 4.0.4 on 2022-05-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_user_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usersecresult',
            field=models.TextField(default='sec result'),
        ),
        migrations.AddField(
            model_name='user',
            name='userthirdresult',
            field=models.TextField(default='third result'),
        ),
    ]
