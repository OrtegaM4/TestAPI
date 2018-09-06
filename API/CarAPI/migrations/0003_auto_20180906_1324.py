# Generated by Django 2.0.3 on 2018-09-06 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarAPI', '0002_auto_20180906_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]