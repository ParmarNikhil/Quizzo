# Generated by Django 3.2.5 on 2021-07-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20210701_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_given',
            field=models.BooleanField(default=False),
        ),
    ]
