# Generated by Django 3.1.7 on 2021-07-01 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0002_userresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresult',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='username',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
