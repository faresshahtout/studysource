# Generated by Django 4.0.4 on 2022-05-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('star_rating', models.IntegerField(max_length=5)),
                ('submission', models.CharField(max_length=250)),
            ],
        ),
    ]
