# Generated by Django 2.0.3 on 2018-09-06 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='highlighted',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cars',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
