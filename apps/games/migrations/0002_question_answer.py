# Generated by Django 3.0.2 on 2020-01-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='Non lo so', max_length=50),
        ),
    ]
