# Generated by Django 2.0.3 on 2018-03-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qSite', '0002_auto_20180325_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-dateTime']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-dateTime']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title of the question'),
        ),
    ]
