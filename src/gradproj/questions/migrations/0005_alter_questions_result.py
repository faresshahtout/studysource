# Generated by Django 4.0.4 on 2022-05-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_questions_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='result',
            field=models.CharField(default='not taking test yet', max_length=70),
        ),
    ]
